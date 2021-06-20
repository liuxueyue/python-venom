#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from ddt import ddt,unpack,data
import unittest
import os
import sys
sys.path.append(os.getcwd())
from common.mars.release_bug.release_bug import ReleaseBugData

@ddt
class ReleaseBugCase(unittest.TestCase):
	@data(*ReleaseBugData().get_diagramId_cost())
	def test_diagramId_ecpend_bug(self,battleDiagram_data):
		self._testMethodDoc = f"测试key == {battleDiagram_data['cKey']}\n【欧美】- 12.10线上bug：battleDiagram.csv 表中 diagramId$cs ID1001~3024  字段ecpend2$cs 消耗[['tool',XXX,数量]]必定为10    ID 4001~4030    字段ecpend2$cs 消耗[['tool',XXX,数量]]必定为20\n"
		diagramId = int(battleDiagram_data['diagramId'])
		for cost in battleDiagram_data['ecpend2']:
			if diagramId <= 3024:
				self.assertEqual(cost[-1],10,f"diagramId = {diagramId} 消耗物品必等于10")
			else:
				self.assertEqual(cost[-1],20,f"diagramId = {diagramId} 消耗物品必等于20")
