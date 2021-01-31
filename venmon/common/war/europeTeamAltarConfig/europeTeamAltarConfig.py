#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : liuxueyue@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
import copy
from common.singleton import Singleton


class europeTeamAltarConfig_data(CommonBase,metaclass=Singleton):


    def __init__(self):
        super().__init__()
        self.config = CommonLoad("europeTeamAltarConfig").get_all_data()


    def card_in_team(self):
        team = CommonLoad("team").get_all_data().items()
        key_data = []
        for k, v in self.config.items():
            key_data.append([self.copy_key_to_value(k, v), team])
        return key_data
