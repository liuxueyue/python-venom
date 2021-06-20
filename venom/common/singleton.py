#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @Author  : wangcunzhu@playcrab.com
# @Desc    :
import weakref

class Singleton(type):
    """这是单例模式的方法

    Args:
        type ([type]): [description]
    """
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Cached(type):
    """这个缓存实例模式的方法

    Args:
        type ([type]): [description]
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj