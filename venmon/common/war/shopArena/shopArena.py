#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : liuxueyue@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
import copy
from common.singleton import Singleton


class shopArena_data(CommonBase,metaclass=Singleton):


    def __init__(self):
        super().__init__()
        self.config = CommonLoad("shopArena").get_all_data()


    def num_test(self):
        key_data = []
        for k, v in self.config.items():
            key_data.append(self.copy_key_to_value(k, v))
        return key_data



    def key_in_tool(self):
        tool = CommonLoad("tool").get_all_data().keys()
        key_data = []
        for k, v in self.config.items():
            key_data.append([self.copy_key_to_value(k, v), tool])
        return key_data


    def costType_in_static(self):
        static = CommonLoad("static").get_all_data().values()
        key_data = []
        static_list = []
        for _v in static:
            static_list.append(_v['name'])
        for k, v in self.config.items():
            key_data.append([self.copy_key_to_value(k, v), static_list])
        return key_data


    def grid_in_setting(self):
        setting = CommonLoad("setting").get_all_data()
        key_data = []
        for k, v in self.config.items():
            key_data.append([self.copy_key_to_value(k, v), setting])
        return key_data


    def level_in_setting(self):
        key_data = []
        for k, v in self.config.items():
            key_data.append(self.copy_key_to_value(k, v))
        return key_data

#shopArena_data().costType_in_static()
