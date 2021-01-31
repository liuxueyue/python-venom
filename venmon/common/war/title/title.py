#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : liuxueyue@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
import copy
from common.singleton import Singleton

class TitleData(CommonBase,metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.config = CommonLoad("title").get_all_data()


    def get_id_key(self):
        key_data = []
        for k, v in self.config.items():
            key_data.append(self.copy_key_to_value(k, v))
        return key_data

    # def in_lang(self):
    #     key_data = []
    #     lang = CommonLoad("lang").get_all_data().keys()
    #     for k,v in self.config.items():
    #         key_data.append([self.copy_key_to_value(k,v),lang])
    #     return key_data