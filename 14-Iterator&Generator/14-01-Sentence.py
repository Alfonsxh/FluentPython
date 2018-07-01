"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 14-01-Sentence.py
@time: 18-7-1 下午9:45
@version: v1.0 
"""
import re
import reprlib

RE_WORD = re.compile('\w+')


def PrintSentence(object):
    print("Begin test {cls}.\n".format(cls=object.__class__.__name__))
    print(object)

    for word in object:
        print(word)

    print(list(object))
    print("End....................\n\n")


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "{className}({printStr})".format(className=self.__class__.__name__, printStr=reprlib.repr(self.text))


# 版本1，使用__getitem__方法替代__iter__方法实现迭代
class Sentence1(Sentence):
    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)


PrintSentence(Sentence1("Hello my world!Hello my world!Hello my world!Hello my world!Hello my world!!"))


# 版本2，典型的迭代器，类中实现__iter__、__next__方法，使用专用的迭代器
class Sentence2(Sentence):
    def __iter__(self):
        return SentenceIterator2(self.words)


class SentenceIterator2:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self


PrintSentence(Sentence2("Hello  world!Hello my world!"))


# 版本3，使用生成器函数
class Sentence3(Sentence):
    def __iter__(self):
        for word in self.words:
            yield word
        return


PrintSentence(Sentence3("Hello  world!Hello my world!"))


# 版本4，惰性实现。前面的版本都在初始化时将text初始化为列表，非惰性实现。
class Sentence4(Sentence):
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


PrintSentence(Sentence4("Hello  world!Hello my world!"))


# 版本5，生成器表达式
class Sentence5(Sentence4):
    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


PrintSentence(Sentence5("Hello  world!Hello my world!"))
