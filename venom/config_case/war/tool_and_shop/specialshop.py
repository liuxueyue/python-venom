#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from ddt import ddt,data,unpack
import unittest
import os,sys
sys.path.append(os.getcwd())
from common.war.tool_and_shop.specialshop import SpecialShopData

@ddt
class specialshop(unittest.TestCase):
    """war.config.specialshop.csv"""
    @data(*SpecialShopData().all_config())
    def test_base(self,specialshop):
        #配置表基础配置测试
        self._testMethodDoc = f"测试id == {specialshop['cKey']}\n配置表基础测试"
        _id = int(specialshop['cKey'])
        self.assertIn(specialshop["tipstype"],"12","tipstype字段异常")
        self.assertIsNotNone(specialshop.get('reset',None),"reset字段异常")
        self.assertNotEquals(specialshop["numlimit"],"0","numlimit字段异常")
        self.assertTrue(0<=int(specialshop["level"])<=110,"level字段异常")
        self.assertTrue(0<=int(specialshop["vip"])<=18,"level字段异常")
        self.assertIsNotNone(specialshop.get('order',None),"order字段异常")
        self.assertIsNotNone(specialshop.get('confirm',None), "confirm字段异常")
        self.assertIn(int(specialshop["timetype"]), (1, 2, 3), f"{specialshop['timetype']} 不处于123区间")
        self.assertIsNotNone(specialshop.get("currency", None),f"currency字段异常")
        if _id > 799999 or _id < 700004:
            self.assertIsNone(specialshop.get("weekShowTime",None),"不应存在weekShowTime")
        if _id < 100001 or _id > 119999:
            self.assertIsNone(specialshop.get("gtype", None), "不应存在gtype")

    @data(*SpecialShopData().in_cashGoodsLib())
    @unpack
    def test_goodsid(self,specialshop,cashGoodsLib_data):
        #goodsid不为空且存在于cashGoodsLib表中
        self._testMethodDoc = f"测试id = {specialshop['cKey']}\ngoodsid不为空且存在于cashGoodsLib表中"
        self.assertIsNotNone(specialshop.get("goodsid",None),f"{specialshop['cKey']} - goodsid 为空")
        self.assertIn(specialshop['goodsid'],cashGoodsLib_data,f"{specialshop['cKey']} - 不存在于cash good lib 为空")

    @data(*SpecialShopData().id_in_100001_100099())
    def test_id(self,specialshop_data):
        self._testMethodDoc = f"测试id = {specialshop_data['cKey']}\nid在100001~100099 gtype$cs=1"
        self.assertEqual(specialshop_data.get("gtype"),"1","id在100001~100099 gtype应当等于1")

    @data(*SpecialShopData().id_in_110000_119999())
    def test_id_2(self,specialshop_data):
        self._testMethodDoc = f"测试id = {specialshop_data['cKey']}\nid在110000_119999 gtype$cs=2"
        self.assertEqual(specialshop_data.get("gtype"),"2","id在110000_119999 gtype应当等于1")

    @data(*SpecialShopData().get_currency_test(14))
    def test_currency_is_14(self,specialshop_data):
        #currency$cs为14时gemprice必定不为空,discount2必定为空
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]}\ncurrency为14时gemprice必定不为空且大于0'
        self.assertIsNotNone(specialshop_data.get("gemprice"),f"{specialshop_data['cKey']}-gemprice字段异常")
        self.assertTrue(int(specialshop_data['gemprice']) > 0,f"{specialshop_data['cKey']}-gemprice小于0")
        self.assertIsNone(specialshop_data.get("discount2",None),f"{specialshop_data['cKey']}-discount2存在脏数据")

    @data(*SpecialShopData().get_currency_test(2))
    def test_currency_is_2(self,specialshop_data):
        #currency$cs为2时gemprice必定为空且discount1为空
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]}\ncurrency为2时gemprice必定为空'
        self.assertIsNone(specialshop_data.get("gemprice",None),f"{specialshop_data['cKey']}-gemprice字段异常")
        self.assertIsNone(specialshop_data.get("discount1", None), f"{specialshop_data['cKey']}-discount1字段异常")

    @data(*SpecialShopData().get_currency_test(3))
    def test_currency_is_3(self,specialshop_data):
        #currency$cs为3时gemprice必定不为空
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]}\ncurrency为3时gemprice必定不为空且大于0'
        self.assertIsNotNone(specialshop_data.get("gemprice"),f"{specialshop_data['cKey']}-gemprice字段异常")
        self.assertTrue(int(specialshop_data['gemprice']) > 0,f"{specialshop_data['cKey']}-gemprice小于0")

    @data(*SpecialShopData().get_discount())
    def test_discount(self,specialshop_data):
        #discount1与discount2互斥，且值处于1-1000，必须被10整除
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]}\n且值处于1-1000，必须被10整除,特殊情况下互斥'
        d1,d2 = specialshop_data.get("discount1",None),specialshop_data.get("discount2",None)
        if specialshop_data["currency"] != "3":
            if specialshop_data.get("discount1"):
                self.assertIsNone(specialshop_data.get("discount2",None),f"{specialshop_data['cKey']}-discount字段异常")
            else:
                self.assertIsNotNone(specialshop_data.get("discount2",None),f"{specialshop_data['cKey']}-discount字段异常")

        if d1:
            self.assertEqual(0, int(d1) % 10, "discount无法被10整除")
            self.assertTrue(1<=int(d1)<=999,"discount数值区间异常")
        if d2:
            self.assertEqual(0, int(d2) % 10, "discount无法被10整除")
            self.assertTrue(1<=int(d2)<=999,"discount数值区间异常")

    @data(*SpecialShopData().in_hero())
    @unpack
    def test_hero_in_heros(self,specialshop_data,hero):
        #hero$cs  hero表中包含
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]} \n验证发放的英雄是否存在于Heor表且show字段是否为1'
        self.assertIn(specialshop_data["hero"],hero.keys(),f"{specialshop_data['cKey']} - hero$cs配置不存在于hero表中")
        self.assertEqual(hero[specialshop_data["hero"]].get("visible"),"1",f"{specialshop_data['cKey']} - hero正常显示")

    @data(*SpecialShopData().in_team())
    @unpack
    def test_team_in_teams(self,specialshop_data,team):
        #team$cs  tema表中包含
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]} \n验证发放的兵团是否存在于team表且show字段是否为1'
        self.assertIn(specialshop_data["team"],team.keys(),f"{specialshop_data['cKey']} - team$cs配置不存在于hero表中")
        self.assertEqual(team[specialshop_data["team"]].get("show"),1,f"{specialshop_data['cKey']} - team正常显示")

    @data(*SpecialShopData().in_treasure())
    @unpack
    def test_treasure_in_treasure(self,specialshop_data,comTreasure,treasureMerchant):
        #treasure$cs  treasure表中包含
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]} \n验证发放的宝物是否存在于treasure表且show字段是否为1'
        self.assertIn(specialshop_data["treasure"],comTreasure.keys(),f"{specialshop_data['cKey']} -  treasure$cs配置不存在于 treasure表中")
        self.assertEqual(comTreasure[specialshop_data["treasure"]].get("display"),"1",f"{specialshop_data['cKey']} -  treasure正常显示")
        self.assertEqual(treasureMerchant[specialshop_data["treasure"]]["allow_open"],"1","treasureMerchant allow_open异常")

    @data(*SpecialShopData().get_invisible())
    @unpack
    def test_invisible_in_config(self,specialshop_data,heroSkin_data,tool_data):
        #测试皮肤数组是否合规[1,x,x] 第2、3id处于配置表中
        self._testMethodDoc = f"测试id == {specialshop_data['cKey']}\n测试invisible字段配置是否合规、是否存于heroskin与tool表"
        self.assertEqual(len(specialshop_data["invisible"]),3,"invisible数组长度异常")
        self.assertIn(str(specialshop_data["invisible"][-1]),heroSkin_data,"invisible配置的皮肤为处于heroskin中")
        self.assertIn(str(specialshop_data["invisible"][1]), tool_data, "invisible配置的皮肤为处于tool中")

    @data(*SpecialShopData().timetype_is_1())
    def test_timetype_is_1(self,specialshop_data):
        #timetype$cs  为1 starttime$cs   endtime$cs 不为空，且starttime$cs <endtime$cs  ，值一定为整数
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]}\n测试timetype为1时的时间类型、大小、判空'
        self.assertIsNotNone(specialshop_data["starttime"],f"{specialshop_data['cKey']} starttime为空")
        self.assertIsNotNone(specialshop_data["endtime"], f"{specialshop_data['cKey']} endtime为空")
        self.assertTrue(int(specialshop_data["endtime"])>int(specialshop_data["starttime"]),f"{specialshop_data['cKey']} end < start")

    @data(*SpecialShopData().timetype_is_2_or_3())
    def test_timetype_is_2_or_3(self,specialshop_data):
        #timetype$cs  为2   starttime$cs   endtime$cs为2017/8/10  5:00:00格式
        self._testMethodDoc = f'测试id = {specialshop_data["cKey"]} \n验证starttime与endtime是否符合格式'
        import time
        def is_time(time_str):
            try:
                #不知道程序怎么处理的，需要确认
                time.strptime(time_str, "%Y-%m-%d %H:%M")
                return True
            except ValueError:
                return False

        self.assertTrue(is_time(specialshop_data["starttime"]),f"{specialshop_data['cKey']} - starttime 格式错误")
        self.assertTrue(is_time(specialshop_data["endtime"]), f"{specialshop_data['cKey']} - endtime 格式错误")
        start_time = int(time.mktime(time.strptime(specialshop_data["starttime"],"%Y-%m-%d %H:%M")))
        end_time = int(time.mktime(time.strptime(specialshop_data["endtime"],"%Y-%m-%d %H:%M")))
        self.assertTrue(end_time > start_time, f"{specialshop_data['cKey']} 结束时间小于开始时间")

    @data(*SpecialShopData().get_weekShowTime())
    def test_week_show_time(self,specialshop_data):
        #用例说明  ID>=700004   小于799999 时，字段一定不为空。取值为星期
        self._testMethodDoc = f"测试id == {specialshop_data['cKey']}\nID>=700004   小于799999 时，字段一定不为空。取值为星期"
        self.assertIsNotNone(specialshop_data.get("weekShowTime",None),"weekShowTime未配置")
        self.assertIsInstance(specialshop_data["weekShowTime"],list,"weekShowTime格式错误")
        self.assertEqual("3",specialshop_data["timetype"],"timetype字段异常")
        self.assertTrue(int(specialshop_data["weekShowTime"][0]) < int(specialshop_data["weekShowTime"][1]),"星期顺序配置错误")
        self.assertEqual("2",specialshop_data["reset"],"reset字段配置错误")
        for day in specialshop_data["weekShowTime"]:
            self.assertTrue(1<=int(day)<=7,"weekShowTime日期配置错误")