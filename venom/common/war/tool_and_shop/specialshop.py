#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
import copy
from common.singleton import Singleton

class SpecialShopData(CommonBase,metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.config = CommonLoad("specialshop").get_all_data()

    def timetype_is_2_or_3(self):
        # key = "timetype_is_2_or_3"
        test_data = []
        for k,v in self.config.items():
            if v["timetype"] == "2" or v["timetype"] == "3":
                test_data.append(self.copy_key_to_value(k,v))
        return test_data

    def timetype_is_1(self):
        test_data = []
        for k,v in self.config.items():
            if v["timetype"] == "1":
                test_data.append(self.copy_key_to_value(k, v))
        return test_data

    def all_config(self):
        test_data = []
        for k,v in self.config.items():
            test_data.append(self.copy_key_to_value(k, v))
        return test_data

    def in_hero(self):
        test_data = []
        heros = CommonLoad("hero").get_all_data()
        for k,v in self.config.items():
            if v.get("hero"):
                test_data.append([self.copy_key_to_value(k, v),heros])
        return test_data

    def in_team(self):
        test_data = []
        team = CommonLoad("team").get_all_data()
        for k,v in self.config.items():
            if v.get("team"):
                test_data.append([self.copy_key_to_value(k, v),team])
        return test_data


    def in_treasure(self):
        test_data = []
        treasure = CommonLoad("comTreasure").get_all_data()
        treasureMerchant = CommonLoad("treasureMerchant").get_all_data()
        for k,v in self.config.items():
            if v.get("treasure"):
                test_data.append([self.copy_key_to_value(k, v),treasure,treasureMerchant])
        return test_data


    def in_cashGoodsLib(self):
        test_data = []
        cashGoodsLib = CommonLoad("cashGoodsLib").get_all_data().keys()
        for k,v in self.config.items():
            test_data.append([self.copy_key_to_value(k,v),cashGoodsLib])
        return test_data

    def id_in_100001_100099(self):
        test_data = []
        for k,v in self.config.items():
            if 100001 <= int(k) <= 100099:
                test_data.append(self.copy_key_to_value(k, v))
        return test_data


    def id_in_110000_119999(self):
        test_data = []
        for k,v in self.config.items():
            if 110000 <= int(k) <= 119999:
                test_data.append(self.copy_key_to_value(k, v))
        return test_data

    def get_currency_test(self,_type):
        test_data = []
        for k,v in self.config.items():
            if v["currency"] in str(_type):
                test_data.append(self.copy_key_to_value(k, v))
        return test_data

    def get_discount(self):
        test_data = []
        for k,v in self.config.items():
            if v.get("discount1") or v.get("discount2"):
                test_data.append(self.copy_key_to_value(k, v))
        return test_data
    
    def get_invisible(self):
        test_data = []
        hero_skin = CommonLoad("heroSkin").get_all_data().keys()
        tool = CommonLoad("tool").get_all_data().keys()
        for k,v in self.config.items():
            if v.get("invisible"):
                test_data.append([self.copy_key_to_value(k, v),hero_skin,tool])
        return test_data

    def get_weekShowTime(self):
        test_data = []
        for k,v in self.config.items():
            if 700004<=int(k)<=799999:
                test_data.append(self.copy_key_to_value(k, v))
        return test_data


if __name__ == "__main__":
    test = SpecialShopData()
    for k,v in test.config.items():
        print(v["numlimit"],type(v["numlimit"]))

        



