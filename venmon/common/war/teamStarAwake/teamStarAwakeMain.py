#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
from common.singleton import Singleton


class TeamStarAwakeMainData(CommonBase, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.config = CommonLoad("teamStarAwakeMain").get_all_data()

    def all_config(self):
        test_data = []
        for k, v in self.config.items():
            test_data.append(self.copy_key_to_value(k, v))
        return test_data


if __name__ == "__main__":
    test = TeamStarAwakeMainData()
    print(test.get_part_data())







