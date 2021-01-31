#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
from common.singleton import Singleton


class TeamStarAwakePartData(CommonBase, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.config = CommonLoad("teamStarAwakePart").get_all_data()
        print(self.config)

    def all_config(self):
        test_data = []
        for k, v in self.config.items():
            test_data.append(self.copy_key_to_value(k, v))
        return test_data

    def get_attr(self):
        test_data = []
        teamStarAwakeIndex = CommonLoad("teamStarAwakeIndex").get_all_data()
        for k,v in self.config.items():
            awake = False
            if teamStarAwakeIndex[k[1:][:-3]].get("isAwake"):
                awake = True
            test_data.append([self.copy_key_to_value(k,v),awake])
        return test_data

    def get_key_nums(self):
        all_key_nums = len(list(self.config.keys()))
        return [all_key_nums]

    def get_cost(self):
        test_data = []
        tool = CommonLoad("tool").get_all_data().keys()
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),tool])
        return test_data

    def get_nums_eq_6(self):
        test_data = []
        tmp_key = []
        for k,v in self.config.items():
            id_last = k[-1]
            id_first = k[:-3]
            if f"{id_first}_{id_last}" not in tmp_key:
                tmp_key.append(f"{id_first}_{id_last}")

        for k in tmp_key:
            tmp_dict = {}
            for index in range(1,7):
                key = k.replace("_",f"{index}0")
                tmp_dict[key] = {
                    "score": self.config[key]['score'],
                    "cost": self.config[key]['cost']
                }
            test_data.append({k:tmp_dict})

        return test_data

    def get_in_lang_data(self):
        test_data = []
        lang = CommonLoad("lang").get_all_data().keys()
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),lang])
        return test_data


if __name__ == "__main__":

    test = TeamStarAwakePartData()












