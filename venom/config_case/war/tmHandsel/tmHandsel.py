from ddt import ddt,data,unpack
import unittest
import os,sys
sys.path.append(os.getcwd())
from common.war.tmHandsel.tmHandsel import tmHandsel #大小写不符合PEP8

@ddt
class tmHandsel(unittest.TestCase):


    @data(*tmHandsel().tmHandsel_data())
    def test_base(self, tmHandsel_data):
        self._testMethodDoc = f"{tmHandsel_data['cKey']}表结构基础测试"
        self.assertEqual(tmHandsel_data['cKey'][:5], tmHandsel_data['hero'], f"{tmHandsel_data['cKey']}ID规则与hero列不符")
        # tmHandsel_data['cKey'][-2:]是"00","01"类型的字符串，转int为了去掉0，配合tmHandsel_data['stage']
        self.assertEqual(int(tmHandsel_data['cKey'][-2:]), int(tmHandsel_data['stage']), f"{tmHandsel_data['cKey']}ID规则与hero列不符")


    @data(*tmHandsel().speak_in_lang())
    @unpack
    def test_in_lang(self, tmHandsel_data, lang):
        self._testMethodDoc = f"{tmHandsel_data['cKey']}描述 在lang表中"
        self.assertIn(tmHandsel_data.get('tips')[0], lang, "tips不再语言表中")
        if tmHandsel_data['stage'] < '10':#可以通过循环编写，另外get用法与断言结合不准确，如果没有返回None，同样会报错，目前这么写会把bug转化成报错
            self.assertIn(tmHandsel_data.get('likeTalk', None), lang, "likeTalk不再语言表中")
            self.assertIn(tmHandsel_data.get('normalTalk', None), lang, "normalTalk不再语言表中")
            self.assertIn(tmHandsel_data.get('hateTalk', None), lang, "hateTalk不再语言表中")


    @data(*tmHandsel().fool_in_tmProduct())
    @unpack
    def test_in_tmProduct(self, tmHandsel_date, tmProduct_data):
        self._testMethodDoc = f"{tmHandsel_date['cKey']}英雄每个等级不同程度的菜品ID是否符合规则"
        lis_1 = []
        if tmHandsel_date['stage'] != '10':#这种if不应当出现在用例里
            for i in tmHandsel_date['like']:#这里还可以优化，没想出好的思路
                lis_1.append(int(i))
                self.assertNotIn(i, tmHandsel_date['normal'], f"likeID{i}与normalID重复")
                self.assertNotIn(i, tmHandsel_date['hate'], f"likeID{i}与hateID重复")
            for k in tmHandsel_date['normal']:
                lis_1.append(int(k))
                self.assertNotIn(k, tmHandsel_date['like'], f"normal{k}与likeID重复")
                self.assertNotIn(k, tmHandsel_date['hate'], f"normal{k}与hateID重复")
            for n in tmHandsel_date['hate']:
                lis_1.append(int(n))
                self.assertNotIn(n, tmHandsel_date['like'], f"hate{n}与likeID重复")
                self.assertNotIn(n, tmHandsel_date['normal'], f"hate{n}与normalID重复")
            for m in tmProduct_data:
                self.assertIn(int(m), lis_1, f"{m}不再tmHandsel菜谱中")


    @data(*tmHandsel().reward_in_tool())
    @unpack
    def test_in_tool(self, tmHandsel_data, tool_key):
        self._testMethodDoc = f"{tmHandsel_data['cKey']}英雄每个等级的奖励是否存在"
        if tmHandsel_data['stage'] != '10' and tmHandsel_data['reward'][0] == 'tool':#同上
            self.assertIn(tmHandsel_data['reward'][1], tool_key, f"{tmHandsel_data['reward']}道具奖励不再tool中")