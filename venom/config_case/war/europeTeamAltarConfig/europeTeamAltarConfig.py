from ddt import ddt,data,unpack
import unittest
import os,sys
sys.path.append(os.getcwd())
from common.war.europeTeamAltarConfig.europeTeamAltarConfig import europeTeamAltarConfig_data

@ddt
class europeTeamAltarConfig_data(unittest.TestCase): #用例名不符合规范 _data不符合


    @data(*europeTeamAltarConfig_data().card_in_team())
    @unpack
    def test_card14_in_tool(self,card, team): #函数名叫tool，传参叫team
        self._testMethodDoc = f"card13兵团配置是否在team表中"
        lis_2 = []
        for k, x in team: #循环变量名不符合常规思路 用例中出现循环的逻辑异常，这个循环不应该出现在这里
            if x.get('zizhi') == '1' and x.get('show') == 1: #这里的测试思路比较混乱，出现冗余流程
                lis_2.append(int(k))
        if card['cKey'] == 'card13':
            for x in card['config']:
                self.assertIn(x[0], lis_2, f"{x[0]}兵团不在兵团表13资质中")


    @data(*europeTeamAltarConfig_data().card_in_team()) #和第11行一样，为什么不合并到一个用里？两个测试目的与思路是一致的，没必要分开
    @unpack
    def test_card14_in_team(self,card, team):
        self._testMethodDoc = f"card14 兵团配置是否在team表中"
        lis_2 = []
        for k, x in team:#同上
            if x.get('zizhi') == '2' and x.get('show') == 1:#同上
                lis_2.append(int(k))
        if card['cKey'] == 'card14':
            for x in card['config']:
                self.assertIn(x[0], lis_2, f"{x[0]}兵团不在兵团表14资质中")


    @data(*europeTeamAltarConfig_data().card_in_team())
    @unpack
    def test_card15_in_team(self,card, team):#同上
        self._testMethodDoc = f"card15 兵团配置是否在team表中"
        lis_2 = []
        for k, x in team:
            if x.get('zizhi') == '3' and x.get('show') == 1:
                lis_2.append(int(k))
        if card['cKey'] == 'card15':
            for x in card['config']:
                self.assertIn(x[0], lis_2, f"{x[0]}兵团不在兵团表15资质中")