#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
from common.singleton import Singleton
import copy


class RuneData(CommonBase,metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.config = CommonLoad("rune").get_all_data()

    def get_rune_data(self):
        test_data = []
        for k,v in self.config.items():
            test_data.append(self.copy_key_to_value(k,v))
        return test_data

    def in_lang(self):
        lang_data = CommonLoad("lang").get_all_data().keys()
        test_data = []
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),lang_data])
        return test_data

    def in_attr(self):
        runeAtt_data = CommonLoad("runeAtt").get_all_data().keys()
        test_data = []
        for k,v in self.config.items():
            if k[0] == "9":
                continue
            test_data.append([self.copy_key_to_value(k,v),runeAtt_data])
        return test_data

    def long_key_quality(self):
        test_data = []
        for k,v in self.config.items():
            if len(k) > 5:
                test_data.append(self.copy_key_to_value(k,v))
        return test_data

    def castData(self):
        test_data = []
        for k,v in self.config.items():
            if k[0] != "9" and k[0:3] != "401":
                test_data.append([self.copy_key_to_value(k,v),self.config.keys()])
        return test_data

    def get_9_401_data(self):
        test_data = []
        for k,v in self.config.items():
            if k[0] == "9" or k[0:3] == "401":
                test_data.append(self.copy_key_to_value(k,v))
        return test_data

    def get_fixAddAtt(self):
        test_data = []
        for k,v in self.config.items():
            if v.get("fixAddAtt"):
                test_data.append(self.copy_key_to_value(k,v))
        return test_data

    def get_skill_data(self):
        skill_data = {
            1: CommonLoad("skill").get_all_data().keys(),
            2: CommonLoad("skillPassive").get_all_data().keys(),
            3: CommonLoad("skillCharacter").get_all_data().keys(),
            4: CommonLoad("skillAttackEffect").get_all_data().keys()
        }
        test_data = []
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),skill_data])
        return test_data