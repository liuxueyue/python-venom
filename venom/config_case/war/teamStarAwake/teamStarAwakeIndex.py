#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from ddt import ddt,data,unpack
import unittest
import os,sys
sys.path.append(os.getcwd())
from common.war.teamStarAwake.teamStarAwakeIndex import TeamStarAwakeIndexData

@ddt
class teamStarAwakeIndex(unittest.TestCase):
    @data(*TeamStarAwakeIndexData().all_config())
    def test_base(self,teamStarAwakeIndex):
        self._testMethodDoc = f"测试兵团 = {teamStarAwakeIndex['cKey']}\n测试配置表基础字段规则"
        team_id = teamStarAwakeIndex['cKey']
        self.assertEqual(team_id,str(teamStarAwakeIndex["awakeMainId"])[1:],"awakeMainId字段不符合基础规则")
        self.assertEqual(teamStarAwakeIndex["convertGet"],int(f"45{team_id}"),"convertGet不符合基础规则")
        self.assertEqual(teamStarAwakeIndex["convertCost"][0],int(f"3{team_id}"),"convertCost第一个元素非法")
        self.assertEqual(teamStarAwakeIndex["convertCost"][1],int(f"94{team_id}"),"convertCost第二个元素非法")
        self.assertEqual(str(teamStarAwakeIndex['awake1Id']),f"8{team_id}1","awake1Id配置规则非法")
        self.assertEqual(str(teamStarAwakeIndex['awake2Id']), f"8{team_id}2", "awake1Id配置规则非法")
        self.assertEqual(1,teamStarAwakeIndex['scale'],"scale字段不为1--临时反推基础验证")
        self.assertEqual(1160, teamStarAwakeIndex['costAll'], "costAll字段不为1160--临时反推基础验证")
        self.assertEqual(teamStarAwakeIndex['raceLabel'],f"raceLabel{team_id}","语言表key定义不规范")

    @data(*TeamStarAwakeIndexData().is_awake_data())
    @unpack
    def test_is_awake_in_team(self,teamStarAwakeIndex_data,team):
        self._testMethodDoc = f"测试兵团 = {teamStarAwakeIndex_data['cKey']}\n测试开启二觉的兵团在team表中是否正确(id,show字段)\n"
        self.assertIn(teamStarAwakeIndex_data['cKey'],team.keys(),"二觉兵团不处于team表中")
        self.assertEqual(team[teamStarAwakeIndex_data['cKey']]["show"],1,"二觉兵团未在team表开启show")
        self.assertIn(str(teamStarAwakeIndex_data['awake1Id']),team.keys(),"awake1Id不处于team表中")
        self.assertIn(str(teamStarAwakeIndex_data['awake2Id']),team.keys(), "awake2Id不处于team表中")


    @data(*TeamStarAwakeIndexData().get_main_id())
    @unpack
    def test_awakeMainId_in_main(self,teamStarAwakeIndex,teamStarAwakeMain_data,main_nums):
        self._testMethodDoc = f"测试兵团 = {teamStarAwakeIndex['cKey']}\n测试主星魂idawakeMainId与Main表关联是否正确、测试key以及数量"
        self.assertEqual(str(teamStarAwakeIndex['awakeMainId']),f"8{teamStarAwakeIndex['cKey']}","与原始id不一致")
        for level in range(1,7):
            _index_id = f"{teamStarAwakeIndex['awakeMainId']}0{level}"
            self.assertIn(_index_id,teamStarAwakeMain_data,f"{_index_id}不存在于teamStarAwakeMain表中")
        self.assertEqual(main_nums[str(teamStarAwakeIndex["awakeMainId"])],6,"awakeMainId不足6个或朱星魂id不存在main表中")


    @data(*TeamStarAwakeIndexData().get_part_data())
    @unpack
    def test_awakePartId_in(self,teamStarAwakeIndex,teamStarAwakePart_data,part_id_nums):
        self._testMethodDoc = f"测试兵团 = {teamStarAwakeIndex['cKey']}\n测试兵团小星魂id是否合规、处于teamStarAwakePart表中，数量是否正确"
        self.assertEqual(6,len(teamStarAwakeIndex["awakePartId"]),"awakePartId长度异常")
        for part in teamStarAwakeIndex["awakePartId"]:
            self.assertEqual(6,part_id_nums[str(part)],"小星魂配置数量异常-teamStarAwakePart表")
            for level in range(1,7):
                self.assertIn(f"{part}0{level}",teamStarAwakePart_data,f"{part}不处于teamStarAwakePart表中")

    @data(*TeamStarAwakeIndexData().get_in_lang_data())
    @unpack
    def test_in_lang(self,teamStarAwakeIndex,lang_data):
        self._testMethodDoc = f"测试兵团 = {teamStarAwakeIndex['cKey']}\n测试raceLabel是否在Lang表中配置"
        self.assertIn(teamStarAwakeIndex['raceLabel'],lang_data,"lang表中不存在")
