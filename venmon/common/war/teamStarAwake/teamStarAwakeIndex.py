#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
from common.singleton import Singleton

class TeamStarAwakeIndexData(CommonBase,metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.config = CommonLoad("teamStarAwakeIndex").get_all_data()
        
    def all_config(self):
        test_data = []
        for k,v in self.config.items():
            test_data.append(self.copy_key_to_value(k,v))
        return test_data

    def is_awake_data(self):
        test_data = []
        team = CommonLoad("team").get_all_data()
        for k,v in self.config.items():
            if v.get("isAwake"):
                test_data.append([self.copy_key_to_value(k,v),team])
        return test_data

    def get_main_id(self):
        test_data = []
        _main_id = {}
        teamStarAwakeMain = CommonLoad("teamStarAwakeMain").get_all_data().keys()
        for _id in teamStarAwakeMain:
            _main_id[_id[:-2]] = _main_id.get(_id[:-2],0) + 1
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),teamStarAwakeMain,_main_id])
        return test_data

    def get_part_data(self):
        test_data = []
        _part_id = {}
        teamStarAwakePart = CommonLoad("teamStarAwakePart").get_all_data().keys()
        for _id in teamStarAwakePart:
            _part_id[_id[:-2]] = _part_id.get(_id[:-2],0) + 1
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),teamStarAwakePart,_part_id])
        return test_data

    def get_in_lang_data(self):
        test_data = []
        lang = CommonLoad("lang").get_all_data().keys()
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),lang])
        return test_data




if __name__ == "__main__":
    test = TeamStarAwakeIndexData()
    print(test.get_part_data())



        



