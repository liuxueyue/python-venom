#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from functools import wraps
from airtest.core.api import *
from datetime import datetime as dt
import time

class DecoratorManager(object):
    @classmethod
    def print_console(cls,desc):
        print(f"playcrab - [{dt.now().strftime('%H:%M:%S.%f')[:-3]}] {desc}")

    @classmethod
    def end_when_exception(cls,desc=None):
        def f(func):
            @wraps(func)
            def wrapper(*args,**kwargs):
                try:
                    result = func(*args,**kwargs)
                    return result
                except Exception as e:
                    snapshot(msg="error snapshot")
                    if desc:
                        log(desc)
                    else:
                        log(e)
                    if not args[0].is_debug:
                        stop_app(args[0].__pkgName__)
                    raise e
                    # todo 后续根据错误码枚举，log()定制化，生成错误类型，钉钉通知等
                    #raise 
            return wrapper
        return f

    @classmethod
    def gm_wait(cls,times=1):
        """执行后等待"""
        def f(func):
            @wraps(func)
            def wrapper(*args, **kw):
                status, result = func(*args, **kw)
                time.sleep(times)
                print(f"{func.__name__} waitting done ...")
                if status == 0:
                    return result
                else:
                    print(f"{func.__name__} Error!!!!!!!!!!")
                    return False
            return wrapper
        return f

    @classmethod
    def time_sleep(cls,times=2,desc=None):
        def f(func):
            @wraps(func)
            def wrapper(*args, **kw):
                func(*args, **kw)
                time.sleep(times)
                print(f"{desc}--{func.__name__} waitting done ...")
            return wrapper
        return f

    @staticmethod
    def performance(f):
        @wraps(f)
        def fn(*args, **kw):
            t_start = time.time()
            r = f(*args, **kw)
            t_end = time.time()
            print('call {}() in {}s'.format(f.__name__, (t_end - t_start)))
            return r
        return fn

    @staticmethod
    def exec_exception_monitor(executer_class, gap:int):
        def wrapper(func):
            @wraps(func)
            def do_func(*args, **kwargs):
                result = func(*args, **kwargs)
                if len(args) >= 2 or kwargs.get("account") != None:
                    return result
                if args[0].get_is_exec_exception_executer():
                    executer_class(gap)
                return result
            return do_func
        return wrapper

    @staticmethod
    def register(name=None):
        if callable(name):
            f = name
            f._register_name = f.__name__
            return f

        def fun_name(f):
            f._register_name = name or f.__name__
            return f
        return fun_name

    @staticmethod
    def stop_monitor_loop_b4_stop_app(func):
        @wraps(func)
        def do_func(hero_base_obj):
            hero_base_obj.__class__.is_exec_exception_executer = False
            time.sleep(3)
            func(hero_base_obj)
        return do_func
