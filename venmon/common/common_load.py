#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : chenfengwu@playcrab.com
# @Desc    :
from common.common_base import CommonBase
import copy, collections
from common.decorator_manager import DecoratorManager
from common.singleton import Singleton

class CommonLoad(CommonBase):
    def __init__(self,json_name):
        super().__init__()
        self.venom_config = self.load_file(f'{self.root_path}/local_config.yaml')["venom"]
        self.__json_data = self.load_file(f"{self.venom_config['JSON_PATH']}/{json_name}.json")

    def get_all_data(self):
        return self.__json_data

    def key_query(self, key_name):
        return self.__json_data.get(key_name,False)

    def get_new_key_data(self, key_name):
        new_data = {}
        for k,v in self.__json_data.items():
            new_data[v[key_name]] = copy.deepcopy(v)
            new_data[v[key_name]]["id"] = k
            del new_data[v[key_name]][key_name]
        return new_data


