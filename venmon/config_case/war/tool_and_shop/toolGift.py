#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from ddt import ddt,unpack,data
import unittest
import os
import sys
sys.path.append(os.getcwd())
from common.war.tool_and_shop.toolGift import ToolGiftData

@ddt
class toolGift(unittest.TestCase):
	# @data(*ToolGiftData().get_all_data())
	# def test_base(self,toolGift):
	# 	self._testMethodDoc = f"测试礼包 = {toolGift['cKey']}\n验证礼包配置基础信息"
	# 	gift_id = toolGift['cKey']
	# 	# self.assertIsNotNone(toolGift.get("getNum",None),"getNum字段为空")
	# 	# self.assertTrue(1<=toolGift['openLv']<=110,"开启等级配置超范围") #openLv可为空？
	# 	self.assertTrue(0<=toolGift.get("openVipLv",1)<=18,"vip等级配置超范围")
	# 	self.assertIsNotNone(toolGift.get("giftContain",None),"礼包配置为空")

	@data(*ToolGiftData().get_all_data())
	def test_temp_base_1(self,toolGift):
		self._testMethodDoc = f"测试礼包 = {toolGift['cKey']}\nvip等级是否正确"
		self.assertTrue(0<=toolGift.get("openVipLv",1)<=18,"vip等级配置超范围")

	@data(*ToolGiftData().get_all_data())
	def test_temp_base_2(self,toolGift):
		self._testMethodDoc = f"测试礼包 = {toolGift['cKey']}\ngetNum是否为空"
		self.assertIsNotNone(toolGift.get("getNum",None),"getNum字段为空")

	@data(*ToolGiftData().get_all_data())
	def test_temp_base_3(self,toolGift):
		self._testMethodDoc = f"测试礼包 = {toolGift['cKey']}\n开启等级是否符合"
		self.assertTrue(1<=toolGift['openLv']<=110,"开启等级配置超范围")

	@data(*ToolGiftData().get_all_data())
	def test_temp_base_4(self,toolGift):
		self._testMethodDoc = f"测试礼包 = {toolGift['cKey']}\n礼包配置是否为空"
		self.assertIsNotNone(toolGift.get("giftContain",None),"礼包配置为空")


	@data(*ToolGiftData().in_tool())
	@unpack
	def test_id_in_tool(self,toolGift,tool_data):
		self._testMethodDoc = f"测试礼包 = {toolGift['cKey']}\n测试是否存在于tool表中"
		self.assertIn(toolGift['cKey'],tool_data)

	@data(*ToolGiftData().reward())
	@unpack
	def test_reward(self,toolGift,tool_data,static_data,avatarFrame_data):
		self._testMethodDoc = f"测试礼包 = {toolGift['cKey']}\n验证物品是否真实存在"
		for reward in toolGift["giftContain"]:
			if "avata" in reward[0]:
				self.assertIn(str(reward[1]),avatarFrame_data,"礼包头像配置不存在")
			elif reward[0] == "tool":
				self.assertIn(str(reward[1]),tool_data,"道具配置不存在")
			else:
				self.assertIn(reward[0],static_data,"资源不存在")