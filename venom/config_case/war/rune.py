#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from ddt import ddt,unpack,data
import unittest
import os
import sys
sys.path.append(os.getcwd())
from common.war.rune.rune import RuneData

@ddt
class rune(unittest.TestCase):
	"""war.config.rune.csv"""
	@data(*RuneData().get_rune_data())
	def test_rune_base(self,rune):
		self._testMethodDoc = f"测试id = {rune['cKey']}\nrune表基础测试"
		self.assertEqual(str(rune["quality"]),rune["cKey"][4],"品质字段一致")
		self.assertEqual(1000, rune["castExp"], "铸造经验应等于1000")
		self.assertTrue(0 < rune["type"] <= 5, "圣徽类型未处于正确区间")
		if rune["quality"] == 2:
			self.assertEqual("435",rune["fightAtt"], "品质2fightAtt属性符合区间")
			self.assertEqual("130", rune["fightAtt2"], "品质2fightAtt2属性符合区间")
			self.assertEqual("1305", rune["fightEffect2"], "品质2fightEffect2属性符合区间")
			self.assertEqual("1305", rune["fightEffect4"], "品质2fightEffect4属性符合区间")
			self.assertEqual("1740", rune["fightEffect6"], "品质2fightEffect6属性符合区间")
			self.assertEqual(rune["castToolNum"], 0, "品质为2时castToolNum == 0")
		elif rune["quality"] == 3:
			self.assertEqual("870",rune["fightAtt"],"品质3fightAtt属性符合区间")
			self.assertEqual("261", rune["fightAtt2"], "品质3fightAtt2属性符合区间")
			self.assertEqual("3914", rune["fightEffect2"], "品质3fightEffect2属性符合区间")
			self.assertEqual("3914", rune["fightEffect4"], "品质3fightEffect4属性符合区间")
			self.assertEqual("5219", rune["fightEffect6"], "品质3fightEffect6属性符合区间")
			self.assertEqual(rune["castToolNum"], 1, "品质为3时castToolNum == 1")
		elif rune["quality"] == 4:
			self.assertEqual("1450",rune["fightAtt"],"品质4fightAtt属性符合区间")
			self.assertEqual("435", rune["fightAtt2"], "品质4fightAtt2属性符合区间")
			self.assertEqual("7829", rune["fightEffect2"], "品质4fightEffect2属性符合区间")
			self.assertEqual("7829", rune["fightEffect4"], "品质4fightEffect4属性符合区间")
			self.assertEqual("10439", rune["fightEffect6"], "品质4fightEffect6属性符合区间")
			self.assertEqual(rune["castToolNum"], 3, "品质为4时castToolNum == 3")
		elif rune["quality"] == 5:
			self.assertEqual("2900",rune["fightAtt"],"品质5fightAtt属性符合区间")
			self.assertEqual("870", rune["fightAtt2"], "品质5fightAtt2属性符合区间")
			self.assertEqual("13048", rune["fightEffect2"], "品质5fightEffect2属性符合区间")
			self.assertEqual("13048", rune["fightEffect4"], "品质5fightEffect4属性符合区间")
			self.assertEqual("17398", rune["fightEffect6"], "品质5fightEffect6属性符合区间")
			self.assertEqual(rune["castToolNum"], 5, "品质为5时castToolNum == 5")

		if rune['cKey'][0] == "9":
			self.assertEqual(401,rune['make'],"id与套装不匹配")
			self.assertEqual([0], rune["integral"], "9系列圣徽integral必须等于[0]")
		else:
			self.assertEqual(int(rune['cKey'][:3]),rune['make'],"id与套装不匹配")
			if rune['cKey'][4] == "5":
				self.assertNotEquals([0],rune["integral"],"品质等于5时integral不应等于[0]")
				if rune.get("addAtt"):
					self.assertNotEquals(rune["integral"], [0], "品质==5 且addAtt$cs 不为空。则integral$cs 必定不等于[0]")
			else:
				self.assertEqual([0],rune["integral"],"品质不等于5时integral应当为[0]")

		if rune.get("basisAtt",False):
			self.assertIsNone(rune.get("fixBasisAtt"),"fixBasisAtt字段不存在")
			self.assertIsNotNone(rune.get("addAtt"), "addAtt存在")
			self.assertIsNone(rune.get("fixAddAtt",None), "fixAddAtt不应存在")
		else:
			self.assertIsNotNone(rune.get("fixBasisAtt",None),"fixBasisAtt应存在")
			self.assertIsNotNone(rune.get("fixAddAtt",None), "fixAddAtty应存在")
			self.assertEqual(2, len(rune["fixBasisAtt"]), "fixBasisAtt长度应当等于2")

		for x in range(2,7,4):
			self.assertEqual(2,len(rune[f"effect{x}"]),f"effect{x} 长度 == 2") #暂时长度是2
			for y in rune[f"effect{x}"]:
				self.assertEqual(2, len(y), "属性投放格式正确[属性id,属性值]")

	@data(*RuneData().get_rune_data())
	def	test_castTool(self,rune):
		#相同圣徽castTool应当一致
		rune_json = RuneData().config
		self._testMethodDoc = f"测试id == {rune['cKey']}\ncastTool应当一致{rune['castTool']}\n{rune_json[rune['cKey'][0:5]]['castTool']}"
		self.assertEqual(rune["castTool"],rune_json[rune["cKey"][0:5]]["castTool"],"同系列圣徽castTool不一致")


	@data(*RuneData().get_rune_data())
	def test_castData(self,rune):
		#用例说明 相同圣徽castData应当一致
		rune_json = RuneData().config
		self._testMethodDoc = f"测试id == {rune['cKey']}\ncastTool应当一致{rune['castData']}\n{rune_json[rune['cKey'][0:5]]['castData']}"
		self.assertEqual(rune["castData"], rune_json[rune["cKey"][0:5]]["castData"], "同系列圣徽castTool不一致")
		for key in rune['castData']:
			self.assertIn(str(key),rune_json.keys(),"配置圣徽未存在于圣徽表中")

	@data(*RuneData().in_lang())
	@unpack
	def test_in_lang(self,rune,lang_data):
		#用例说明
		self._testMethodDoc = f"测试id == {rune['cKey']}\n验证各字段是否存在于lang表中"
		self.assertIn(rune['name'],lang_data,"name未存在于lang表中")
		self.assertIn(rune['des2'], lang_data, "des2未存在于lang表中")
		self.assertIn(rune['des4'], lang_data, "des4未存在于lang表中")
		self.assertIn(rune['des6'], lang_data, "des6未存在于lang表中")
		self.assertIn(rune['shopDes'], lang_data, "shopDes未存在于lang表中")

	@data(*RuneData().get_rune_data())
	def test_extraAtt(self,rune):
		#用例说明 测试品质为5时extraAtt条数==4
		self._testMethodDoc = f"测试id == {rune['cKey']}\n测试品质为5时extraAtt条数==4"
		self.assertEqual(0<=rune["extraAtt"]<=4,True,"extraAtt必定小于等于4")
		if rune["quality"] == 5:
			self.assertEqual(4, rune["extraAtt"], "extra应当等于4")
		else:
			self.assertNotEquals(4, rune["extraAtt"], "extraAtt应当 != 4")

	@data(*RuneData().in_attr())
	@unpack
	def test_in_runeAttr(self,rune,runeAtt_data):
		#用例说明 测试basisAtt、addAtt是否存在于runeAtt表、基础圣徽与高级圣徽配置是否符合规范
		self._testMethodDoc = f"测试id == {rune['cKey']}\n测试basisAtt、addAtt是否存在于runeAtt表、基础圣徽与高级圣徽配置是否符合规范"
		if len(rune["cKey"]) == 5:
			self.assertIn(str(rune["basisAtt"]),runeAtt_data,"basisAtt 未存在与runeAtt表中")
			self.assertIn(str(rune["addAtt"]), runeAtt_data, " addAtt 存在与runeAtt表中")
		else:
			self.assertNotEquals(rune.get("basisAtt", False), True, "不应配置basisAtt")
			self.assertNotEquals(rune.get("addAtt", False), True, "不应配置addAtt")

	@data(*RuneData().long_key_quality())
	def test_long_id(self,rune_data):
		#用例说明：测试圣徽长id品质字段是否一定等于5
		self._testMethodDoc = "测试圣徽长id品质字段是否一定等于5"
		self.assertEqual(rune_data['cKey'][4],"5","长id品质必定等于5")

	@data(*RuneData().castData())
	@unpack
	def test_castData_value_not_9(self, rune_data,rune_all_key):
		#用例说明 测试castData字段中的值是否符合规范（品质=5时castData中的值前3位必定一样且存在于rune表，品质!=5时必定等于自己）
		self._testMethodDoc = f"测试id == {rune_data['cKey']}\n测试castData字段中的值是否符合规范（品质=5时castData中的值前3位必定一样且存在于rune表，品质!=5时必定等于自己）\n9系列与401未测试"
		for x in rune_data["castData"]:
			if rune_data["cKey"][4] == "5":
				self.assertEqual(rune_data["cKey"][0:4],str(x)[0:4],"品质为5，castData字段内容中id前4位必定一致")
				self.assertIn(str(x),rune_all_key,"castData字段中内容必定存在于rune表")
			else:
				self.assertEqual(int(rune_data["cKey"]),x,"品质不为5，castData字段必定等于自己")

	@data(*RuneData().get_9_401_data())
	def test_castData_value_in_9(self,rune_data):
		#用例说明 验证9系列与401，特殊规则
		self._testMethodDoc = f"测试id == {rune_data['cKey']}\n测试castData字段中的值是否符合规范:特殊9系列与401"
		rune_json = RuneData().config
		castData_401 = rune_json["40105"]["castData"]
		# print(f"开始测试{rune_data['cKey']}")
		if rune_data['cKey'][0:5] == "40105":
			self.assertEqual(castData_401,rune_data['castData'])
		for key in rune_data['castData']:
			if rune_data['cKey'][0] == "9":
				special = str(key).replace("4010","9000")
				self.assertEqual(special[0:5],rune_data['cKey'][0:5],"castData字段异常")
			else:
				special = str(key).replace("9000","4010")
				self.assertEqual(special[0:5],rune_data['cKey'][0:5],"castData字段异常")
			self.assertIn(str(key),rune_json.keys(),"castData中的数据存在于rune表")


	@data(*RuneData().get_9_401_data())
	def test_integral_9(self,rune_data):
		#用例说明 单独测试9xxxx系列圣徽integral字段
		self._testMethodDoc = f"测试id == {rune_data['cKey']}\n单独测试9xxxx系列圣徽integral字段"
		if rune_data['cKey'][0] == "9":
			self.assertEqual([0], rune_data["integral"], "9系列圣徽integral应当等于[0]")
		else:
			if rune_data["quality"] == 5:
				self.assertNotEquals([0],rune_data["integral"],"品质等于5时integral应当不等于[0]")
			else:
				self.assertEqual([0],rune_data["integral"],"品质不等于5时应当等于[0]")

	@data(*RuneData().get_fixAddAtt())
	def test_fixAddAtt(self,rune_data):
		#绿色=1条
		#蓝色=最多2条，最少1条
		#紫色=最多3条，最少2条
		#橙色=最多4条，最少3条
		#属性id 必定小于等于92，属性最大值不超过100
		self._testMethodDoc = f"测试id = {rune_data['cKey']}\n绿色=1条属性、蓝色最多2条最少1条，紫色最多3条最少2条，橙色最多4条最少3条\n属性id 必定小于等于92，属性最大值不超过100"
		if rune_data["quality"] == 2:
			self.assertTrue(1==len(rune_data["fixAddAtt"]),f"品质{rune_data['quality']}时长度必定=1")
		elif rune_data["quality"] == 3:
			self.assertTrue(1<=len(rune_data["fixAddAtt"])<=2,f"品质{rune_data['quality']}时长度必定最多2条，最少1条")
		elif rune_data["quality"] == 4:
			self.assertTrue(2<=len(rune_data["fixAddAtt"])<=3,f"品质{rune_data['quality']}时长度必定最多3条，最少2条")
		elif rune_data["quality"] ==5:
			self.assertTrue(3<=len(rune_data["fixAddAtt"])<=4,f"品质{rune_data['quality']}时长度必定最多4条，最少3条")

	@data(*RuneData().get_skill_data())
	@unpack
	def	test_effect4(self,rune,skill_data):
		#测试effect4字段所配置技能是否存在
		self._testMethodDoc = f"测试id = {rune['cKey']}\n测试effect4字段所配置技能是否存在"
		for x in rune["effect4"]:
			self.assertIn(str(x[-1]),skill_data[x[0]],"技能未存在于对应skill表中")

	@data(*RuneData().get_rune_data())
	def test_attr_special(self,rune_data):
		#用例说明 测试投放属性值是否符合区间、属性数组长度是否正确
		self._testMethodDoc = f"测试id == {rune_data['cKey']}\n测试投放属性值是否符合区间、属性数组长度是否正确"
		effect_key = ["effect2","effect6"]

		for key in effect_key:
			effect = rune_data[key]
			_make = {}
			for attr in effect:
				self.assertTrue(attr[0] <= 92, "属性id<=92")
				self.assertTrue(attr[1] < 100, "投放属性必定小于100")
				_make[attr[0]] = 1
			self.assertEqual(2,len(_make.keys()),"属性投放重复")

		if rune_data.get('fixBasisAtt'):
			fix_key = ['fixBasisAtt','fixAddAtt']
			for key in fix_key:
				attrs = rune_data[key]
				for attr in attrs:
					self.assertTrue(attr[0] <= 92, "属性id<92")
					self.assertTrue(attr[1] < 100, "投放属性必定小于100")
					if rune_data['cKey'][0] == "9":
						self.assertEqual(3,len(attr),"9系列圣徽属性应当存在权重")
					else:
						self.assertEqual(2, len(attr), "9系列圣徽属性应当存在权重")
