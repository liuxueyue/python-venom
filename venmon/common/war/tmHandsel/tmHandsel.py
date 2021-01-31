#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : liuxueyue@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
import copy
from common.singleton import Singleton


class tmHandsel(CommonBase,metaclass=Singleton):


    def __init__(self):
        super().__init__()
        self.config = CommonLoad("tmHandsel").get_all_data()

    def tmHandsel_data(self):
        tmHandsel_list = []
        for k, v in self.config.items():
            tmHandsel_list.append(self.copy_key_to_value(k, v))
        return tmHandsel_list


    def speak_in_lang(self):
        lang = CommonLoad("lang").get_all_data().keys()
        tmHandsel_list = []
        for k, v in self.config.items():
            tmHandsel_list.append([self.copy_key_to_value(k, v), lang])
        return tmHandsel_list

    def fool_in_tmProduct(self):
        tmProduct = CommonLoad("tmProduct").get_all_data().keys()
        tmHandsel_list = []
        for k, v in self.config.items():
            tmHandsel_list.append([self.copy_key_to_value(k, v), tmProduct])
        return tmHandsel_list

    def reward_in_tool(self):
        tool = CommonLoad("tool").get_all_data().keys()
        tmHandsel_list = []
        for k, v in self.config.items():
            tmHandsel_list.append([self.copy_key_to_value(k, v), tool])
        return tmHandsel_list