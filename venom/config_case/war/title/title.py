#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : liuxueyue@playcrab.com
# @Desc    :
from ddt import ddt,unpack,data
import unittest
import os
import sys
sys.path.append(os.getcwd())
from common.war.title.title import TitleData

@ddt
class title(unittest.TestCase):

    @data(*TitleData().get_id_key())
    def test_id_base(self, title):
        self._testMethodDoc = f"测试id = {title['cKey']}\n基础测试"
        self.assertEqual(title['cKey'][0], str(title['type']), "ID第一位与typeID一致")
        # self.assertIsNotNone(title['cKey'], "ID不能为空")  #不需要
        self.assertIn(title['type'], (1, 2, 3, 4), f"type不处于1234之间")
        self.assertIn(title['titletype'], (1, 2), f"titletype不处于12之间")
        self.assertIsNotNone(title['rank'], "ID不能为空")
        self.assertTrue(title['time'] == -1, "time必须为-1")
        self.assertEqual("SLOGAN_"+ title['cKey'], title['title'], f"title格式命名为SLOGAN_+cKey")#f格式
        self.assertEqual("SLOGANDES_" + title['cKey'], title['titledescription'], f"title描述格式命名为SLOGANDES_+cKey")


    # @data(*Title().in_lang())
    # @unpack
    # def test_title_text_lang(self,title,lang):
    #     self._testMethodDoc = f'测试id = {title["cKey"]} \n称号title描述配置是否存在lang表'
    #     self.assertIn(title["titledescription"],lang.keys(),f"{title['titledescription']} - title_title描述配置不存在lang表中")
