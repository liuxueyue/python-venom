#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    : 

from common.common_base import CommonBase
import os
import csv
import shutil
import copy

class Convert(CommonBase):
	def __init__(self,venom_project,config):
		super().__init__()
		self.venom_project = venom_project
		self.config = config
		self.venom_config = self.config["venom"]
		self.project = self.config[self.venom_project]


	def format_key(self,keystring):
		return keystring.split("$")[0]

	def	csv2json(self,filename):
		csv_data_list = []
		finalResult = {}
		with open(filename, "r", encoding=self.project["CSV_SPECIAL"]) as f:
			reader = csv.reader(f)
			for index, row in enumerate(reader):
				if index == 0:
					keyList = list(map(self.format_key, row))
					if row[0] != "":
						key = (list(map(self.format_key, row)))[0]
					else:
						pass
				elif index == 1:
					keyType = row  # 提取type(程序没有用到，属于策划注释，大部分可能对不上)
				else:
					if index < 5:
						pass  # 前2-4行注释行，没有用无需导入json
					else:
						csv_data_dict = {}  # 转换
						for rownum, value in enumerate(row):  # 按行提取
							if rownum == 0:
								if "#" in value:  # 删除csv中的分割注释
									continue
							if value != '' and keyList[rownum] != '':  # 空value，无效key，空key筛选
								if '[' in value:  # 数组
									try:
										csv_data_dict[keyList[rownum]] = eval(
											value.replace("，", ","))  # 筛选中文逗号后尝试用eval统一数据格式
									except:
										tmpValue = str(value.replace("[", "").replace("]",
																					  ""))  # 特殊处理(012非法Int,int(str)报错处理)，这里无法有效处理多维数组
										csv_data_dict[keyList[rownum]] = tmpValue.split(",")  # 还原数组格式
								else:
									if keyType[rownum] == "int":
										try:
											csv_data_dict[keyList[rownum]] = int(value)  # int转换
										except:
											csv_data_dict[keyList[rownum]] = value
									elif keyType[rownum] == "float":
										try:
											csv_data_dict[keyList[rownum]] = float(value)  # float转换
										except:
											csv_data_dict[keyList[rownum]] = value
									else:
										csv_data_dict[keyList[rownum]] = value  # 字符串处理
						if csv_data_dict != {}:
							csv_data_list.append(csv_data_dict)

		for x in csv_data_list:
			tempKey = False
			if x.get(key):
				tempKey = copy.deepcopy(x[key])
				del x[key]
			if tempKey != False:
				if isinstance(tempKey, list):
					tempKey = str(tempKey)
				tempValue = copy.deepcopy(x)
				finalResult[tempKey] = tempValue
		return finalResult

	def handle_lang(self):
		new_lang = {}
		for x in range(0, 11):
			if not os.path.exists(f"{self.venom_config['JSON_PATH']}/lang_{x}.json"):
				continue
			tmp_ = {}
			print(f"#### operate: [lang_{x}.json]                      ")
			old_lang = self.load_file(f"{self.venom_config['JSON_PATH']}/lang_{x}.json")
			for k, v in old_lang.items():
				if v.get("cn"):
					if type(v["cn"]) == str:
						tmp_[k] = v["cn"].lstrip("#")
					else:
						tmp_[k] = v["cn"]
			new_lang.update(**tmp_)
			os.remove(f"{self.venom_config['JSON_PATH']}/lang_{x}.json")
		self.write_json(os.path.join(self.venom_config["JSON_PATH"],"lang.json"), new_lang)

	def	convert(self):
		if os.path.exists(self.venom_config["JSON_PATH"]):
			shutil.rmtree(self.venom_config["JSON_PATH"])
		os.mkdir(self.venom_config["JSON_PATH"])
		for root, dirs, files in os.walk(os.path.join(self.venom_config["CONFIG_PATH"])):
			for x in files:
				# if x[-3:] == "csv" and x[:4] != "lang":#跳过lang表的处理
				if x[-3:] == "csv":
					filename = x.replace("csv", "json")
					try:
						jsonData = self.csv2json(os.path.join(root, x))
						self.write_json(os.path.join(self.venom_config["JSON_PATH"], filename), jsonData)
						print(f"#### operate: [{x}]                      ")
					except Exception as e:
						print(e)
						print(f"[Error!!!!] Convert {root}/{x} Error")
						continue
		self.handle_lang()

