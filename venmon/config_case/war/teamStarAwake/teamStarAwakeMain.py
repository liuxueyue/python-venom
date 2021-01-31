#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from ddt import ddt,data,unpack
import unittest
import os,sys
sys.path.append(os.getcwd())
from common.war.teamStarAwake.teamStarAwakeMain import TeamStarAwakeMainData

@ddt
class teamStarAwakeMain(unittest.TestCase):
    @data(*TeamStarAwakeMainData().all_config())
    def test_base(self,teamStarAwakeMain):
        self._testMethodDoc = f"测试兵团 = {teamStarAwakeMain['cKey']}\n测试配置表基础字段规则"




