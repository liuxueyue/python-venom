#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from ddt import ddt,data,unpack
import unittest
import os,sys
sys.path.append(os.getcwd())
from common.war.teamStarAwake.teamStarAwakePart import TeamStarAwakePartData

@ddt
class teamStarAwakePart(unittest.TestCase):
    @data(*TeamStarAwakePartData().all_config())
    def test_base(self,teamStarAwakePart):
        const = {
            "1":{
                "pic":"035",
                "effect":"shuixing",
            },
            "2": {
                "pic": "019",
                "effect": "anxing",
            },
            "3": {
                "pic": "028",
                "effect": "qixing",
            },
            "4": {
                "pic": "09",
                "effect": "huoxing",
            },
            "5": {
                "pic": "017",
                "effect": "anniu",
            },
            "6": {
                "pic": "06",
                "effect": "guangxing",
            }
        }
        self._testMethodDoc = f"测试小星魂 = {teamStarAwakePart['cKey']}\n测试配置表基础字段规则"
        _id = teamStarAwakePart['cKey']
        self.assertEqual(f"StarAwakePartName{_id[-3]}",teamStarAwakePart['name'],"name字段规则不规范")
        self.assertEqual(f"TeamTwoAwaken{const[_id[-3]]['pic']}",teamStarAwakePart['pic'],"pic字段规则不规范")
        self.assertEqual(const[_id[-3]]['effect'],teamStarAwakePart['effect'],"effect字段规则不规范")

    @data(*TeamStarAwakePartData().get_attr())
    @unpack
    def test_attr(self,teamStarAwakePart,is_awake):
        self._testMethodDoc = f"测试小星魂 = {teamStarAwakePart['cKey']}\n属性格式、属性id、已开放觉醒是否存在0"
        att_key = ["addProp1", "addProp2"]
        for key in att_key:
            for attr in teamStarAwakePart[key]:
                self.assertTrue(len(attr)==2,"属性投放格式非法")
                self.assertTrue(1<=attr[0]<=92,"属性id非法")
                if is_awake:
                    self.assertTrue(attr[1] > 0, "属性值非法,属性小于等于0")

    @data(*TeamStarAwakePartData().get_key_nums())
    def test_part_nums(self,nums):
        self._testMethodDoc = f"测试星魂数量是否为6,能否被36整除"
        self.assertEqual(0,nums%36,"配置数量无法被36整除，小星魂数量异常")

    
    @data(*TeamStarAwakePartData().get_cost())
    @unpack
    def test_cost(self,teamStarAwakePart,tool_data):
        self._testMethodDoc = f"测试小星魂 == {teamStarAwakePart['cKey']}\n测试消耗配置是否正确，符合顺序、道具是否存在"
        for index,cost in enumerate(teamStarAwakePart['cost']):
            self.assertEqual(cost[0],'tool',"消耗配置非道具")
            self.assertTrue(cost[-1]>0,"消耗数量配置小于等于0")
            self.assertIn(str(cost[1]),tool_data,"消耗配置不存在道具表中")
            if index == 0:
                self.assertEqual(int(f"45{teamStarAwakePart['cKey'][1:][:-3]}"),cost[1],"消耗道具id与兵团id不匹配")
            elif index == 1:
                self.assertEqual(40030,cost[1],"第二个消耗物品不为星魂水晶")


    @data(*TeamStarAwakePartData().get_nums_eq_6())
    def test_cost_and_score_eq(self,teamStarAwakePart_data):
        self._testMethodDoc = f"测试{teamStarAwakePart_data.keys()}系列消耗、战力是否一致"
        for k,v in teamStarAwakePart_data.items():
            # print(list(v.values()))
            # print(set(map(str, list(v.values()))))
            self.assertEqual(1,len(set(map(str, list(v.values()))))) #刺激不，括号多不？

    @data(*TeamStarAwakePartData().get_in_lang_data())
    @unpack
    def test_in_lang(self,teamStarAwakePart,lang_data):
        self._testMethodDoc = f"测试{teamStarAwakePart['cKey']}相关描述是否存于Lang表中"
        self.assertIn(teamStarAwakePart['name'],lang_data,"lang表中不存在")
