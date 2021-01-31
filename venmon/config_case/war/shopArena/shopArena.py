from ddt import ddt,data,unpack
import unittest
import os,sys
sys.path.append(os.getcwd())
from common.war.shopArena.shopArena import shopArena_data

@ddt
class shopArena(unittest.TestCase):


    @data(*shopArena_data().num_test())
    def test_num(self, shopArena_data):
        self._testMethodDoc = f"测试ID = {shopArena_data['cKey']}基础测试"
        self.assertTrue(1<= shopArena_data['num'] <=20, f"{shopArena_data['num']}配置数值超出范围")
        self.assertTrue(1 <= shopArena_data['costNum'] <= 1000, f"{shopArena_data['costNum']}配置数值超出范围")
        self.assertTrue(shopArena_data['costType'] == "currency", f"{shopArena_data['costType']}配置消耗货币错误")


    @data(*shopArena_data().key_in_tool())
    @unpack
    def test_itemId_in_tool(self,shopArenadate, item_data):
        self._testMethodDoc = f"测试ID = {shopArenadate['cKey']}在tool表中"
        for _v in shopArenadate.get('itemId'):
            self.assertIn(str(_v), item_data, f"{shopArenadate}不再在tool表中")


    @data(*shopArena_data().costType_in_static())
    @unpack
    def test_costType_in_static(self, shopArenadate, static_data):
        self._testMethodDoc = f"测试ID = {shopArenadate['cKey']}是否在static"
        self.assertIn(shopArenadate['costType'], static_data, f"{shopArenadate['costType']}不再在static表中")


    @data(*shopArena_data().grid_in_setting())
    @unpack
    def test_grid_setting(self, shopArenadate, setting_data):
        self._testMethodDoc = f"测试ID = {shopArenadate['cKey']}grid边界"
        self.assertTrue(1 <= shopArenadate['grid'][0] <= int(setting_data['G_ARENA_CONTENT'].get('value')), f"{shopArenadate['grid']}格子上限不符合setting配置")


    @data(*shopArena_data().level_in_setting())
    def test_grid_setting(self, shopArenadate):
        self._testMethodDoc = f"测试ID = {shopArenadate['cKey']}level边界"
        self.assertTrue(0 <= shopArenadate['level'][0] and shopArenadate['level'][1] <= 120, f"{shopArenadate['level']}等级边界不符合setting配置")



