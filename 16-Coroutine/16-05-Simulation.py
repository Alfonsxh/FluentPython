"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 16-05-Simulation.py
@time: 18-7-24 下午10:45
@version: v1.0 
"""
# 离散事件仿真----模拟出租车服务
import random
import collections
import queue

# 默认值
DEFAULT_NUMBER_OF_TAXIS = 3
DEFAULT_END_TIME = 180
SEARCH_DURATION = 5
TRIP_DURATION = 20
DEPARTURE_INTERVAL = 5

# 动作枚举
LEAVE_ACTION = "leave garage"
DROP_ACTION = "drop off passenger"
PICK_ACTION = "pick up passenger"
GO_HOME_ACTION = "going home"

Event = collections.namedtuple("Event", "time,proc,action")  # 事件类型，包括时间、乘客、行为


def taxi_process(ident, trips, start_time=0):
    """
    taxi事件处理函数
    :param ident: taxi 编号
    :param trips: 需要接收乘客的次数
    :param start_time: 初始发车事件
    :return:
    """
    time = yield Event(start_time, ident, LEAVE_ACTION)     # 发车
    for i in range(trips):
        time = yield Event(time, ident, PICK_ACTION)    # 接收乘客
        time = yield Event(time, ident, DROP_ACTION)    # 乘客下车
    yield Event(time, ident, GO_HOME_ACTION)        # 处理完所有订单后回家


def compute_duration(previous_action):
    """
    使用指数分布随机生成操作的时长
    :param previous_action: 触发事件的动作
    :return: 操作的时长
    """
    # 根据不同的事件使用不同的时间作为指数分布的参数
    if previous_action in [LEAVE_ACTION, DROP_ACTION]:
        interval = SEARCH_DURATION
    elif previous_action == PICK_ACTION:
        interval = TRIP_DURATION
    elif previous_action == GO_HOME_ACTION:
        interval = 1
    else:
        raise ValueError("Unknow previous_action {action}".format(action=previous_action))
    return int(random.expovariate(1 / interval)) + 1                # 返回指数分布结果


class Simulation:

    def __init__(self, process_map):
        self.events = queue.PriorityQueue()     # 优先队列，如果是tuple元素，则按tuple的第一个元素排序
        self.procs = dict(process_map)          # 避免修改self.procs时同时修改process_map！！

    def run(self, end_time):
        for _, proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.events.put(first_event)

        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print("*** end of events. ***")
                break

            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print("taxi:", proc_id, proc_id * "    ", current_event)

            active_proc = self.procs[proc_id]           # 获取指定出租车的进程
            next_time = sim_time + compute_duration(previous_action)  # 使用指数分布计算操作的耗时，算出下一事件发生的事件
            try:
                next_event = active_proc.send(next_time)            # 执行此次事件，更新下次事件
            except StopIteration:
                del self.procs[proc_id]         # 将任务完成的出租车剔除队列
            else:
                self.events.put(next_event)     # 将下一个时间put进队列
        else:
            # 打印结束时间后仍未完成任务的出租车数
            print("end of simulation time: {} events pending.".format(self.events.qsize()))


def main(end_time=DEFAULT_END_TIME, num_taxis=DEFAULT_NUMBER_OF_TAXIS, seed=None):
    if seed is not None:
        random.seed(seed)

    # 初始化出租车的状态
    taixs = {i: taxi_process(i, (i + 1) * 2, i * DEPARTURE_INTERVAL) for i in range(num_taxis)}

    sim = Simulation(taixs)
    sim.run(end_time)


if __name__ == "__main__":
    main(end_time=200, num_taxis=3)
