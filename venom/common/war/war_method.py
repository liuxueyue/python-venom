#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : chenfengwu@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
import collections
from common.decorator_manager import DecoratorManager
from common.singleton import Singleton

class ToolJson(CommonBase, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.tool_json = CommonLoad("tool").get_all_data()
        self.lang_json = CommonLoad("lang").get_all_data()
        self.team_json = CommonLoad("team").get_all_data()
        self.systemOpen_json = CommonLoad("systemOpen").get_all_data()
        self.setting_json = CommonLoad("setting").get_all_data()

    @DecoratorManager.performance
    def name_query(self,name,art=0):#根据中文名称获取道具id
        """
        name为道具的中文名称
        """
        _tmp = []
        for k,v in self.tool_json.items():
            if "+" == name[-2:-1]:
                art = int(name[-1])
            if name == self.lang_json.get(v["name"],False) and art == v.get("art1",0):
                _tmp.append(k)
        return max(_tmp)

    @DecoratorManager.performance
    def team_name_query(self,name):#根据中文名称获取兵营id
        """
        name为兵团的中文名称
        """
        for k,v in self.team_json.items():
            if name == self.lang_json.get(v["name"],False):
                return k

    @DecoratorManager.performance
    def tool_name(self,name):#根据tool表中name字段获取中文名称
        """
        name为tool表中的name字段
        """
        return self.lang_json[name]

    @DecoratorManager.performance
    def id_tool_name(self,tool_id):#根据id获取tool表中name字段
        """
        tool_id为道具的id，该方法为通过道具id获取tool表中的name字段
        """
        for k,v in self.tool_json.items():
            if k == tool_id:
                return v.get("name")

    @DecoratorManager.performance
    def tool_name_id(self,name):#tool表中name获取id
        """
        name为tool表中的name字段，该方法为通过此name获取tool表中的道具id
        """
        for k,v in self.tool_json.items():
            if name == v["name"]:
                return k

    @DecoratorManager.performance
    def get_tool_json(self):
        """
        获取 tool表的内容
        """
        return self.tool_json

    @DecoratorManager.performance
    def open_lv(self,keword):
        """
        获取对应功能的开启等级
        keword 对应功能的标志位
        """
        for key, value in self.systemOpen_json.items():
            if value["system"] == keword:
                return value["openLevel"]

    @DecoratorManager.performance
    def show_lv(self,keword):
        """
        获取对应功能的开启等级
        keword 对应功能的标志位
        """
        for key, value in self.systemOpen_json.items():
            if value["system"] == keword:
                return value["showLevel"]

    def setting(self,tag):
        """返回setting表的value

        Args:
            tag ([type]): [setting表的tag]

        Returns:
            [type]: [description]
        """
        return self.setting_json[tag]["value"]

    def key_list(self):
        tool_dict = collections.defaultdict(list)
        for key,value in self.tool_json.items():
            if value.get("typeId"):
                tool_dict[value.get("typeId")].append([key,value])
        return dict(tool_dict)

    def race1_team(self):
        """筛选出以阵营为key，兵团id为list数组的数据

        Returns:
            [dict]: [description]
        """
        temp = dict()
        race1_dict = collections.defaultdict(list)
        for k,v in self.team_json.items():
            if v.get("show"):
                temp[k] = v
        for teamid, value in temp.items():
            race1_dict[value.get("race")[0]].append(teamid)
        return race1_dict

    def get_lang_key(self,name):#根据中文名称查询lang表中的key
        for k,v in self.lang_json.items():
            if v == name:
                return k
