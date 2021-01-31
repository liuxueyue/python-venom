#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
from common.singleton import Singleton

class ToolGiftData(CommonBase,metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.config = CommonLoad("toolGift").get_all_data()

    def get_all_data(self):
        test_data = []
        for k,v in self.config.items():
            test_data.append(self.copy_key_to_value(k,v))
        return test_data

    def in_tool(self):
        test_data = []
        tool = CommonLoad("tool").get_all_data().keys()
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),tool])
        return test_data

    def reward(self):
        test_data = []
        static = []
        tool = CommonLoad("tool").get_all_data().keys()
        static_json = CommonLoad("static").get_all_data()
        avatarFrame = CommonLoad("avatarFrame").get_all_data().keys()
        for k,v in static_json.items():
            static.append(v["name"])

        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),tool,static,avatarFrame])
        return test_data




