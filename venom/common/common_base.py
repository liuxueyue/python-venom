#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.decorator_manager import DecoratorManager
import json
import yaml
import os
import copy
import requests
import time

class CommonBase:
	def __init__(self):
		self.root_path = self.get_root_path()

	def get_all_config(self):
		"""返回全部local_config"""
		return self.load_file(f'{self.root_path}/local_config.yaml')

	def get_root_path(self):
		"""用于判断路径"""
		if os.path.join("venom\\common") in __file__:
			return f'{__file__.split("common")[0]}'.rstrip("/")
		elif os.path.join("venom","config_case") in __file__:
			return f'{__file__.split("config_case")[0]}'.rstrip("/")

	def splicing(self,loader, node):
		seq = loader.construct_sequence(node)
		return ''.join([str(i) for i in seq])

	def load_file(self,path):
		"""通用读取文件"""
		if str(os.path.splitext(path)[-1]) == ".yaml":
			yaml.add_constructor('!splicing', self.splicing)
			with open(path, 'r', encoding='utf-8') as yamlFile:
				return yaml.load(yamlFile,Loader=yaml.FullLoader)
		elif str(os.path.splitext(path)[-1]) == ".json":
			with open(path, 'r', encoding='utf-8') as jsonFile:
				return json.load(jsonFile)

	def write_json(self,fileName,filedata,openType="w"):
		"""通用写json文件"""
		with open(fileName,openType,encoding='utf-8') as tempFile:
			tempFile.write(json.dumps(filedata, ensure_ascii=False, sort_keys=False, indent=4))

	def copy_key_to_value(self, key, value):
		"""
		:param key: json.key
		:param value: json.value
		:return: dict {value:{value},cKey:key}
		"""
		#把key存进value,新key为cKey
		tmp_value = copy.deepcopy(value)
		tmp_value["cKey"] = key
		return tmp_value

	def message(self, token, message, name_list=[]):
		url = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)
		HEADERS = {
			"Content-Type": "application/json ;charset=utf-8 "
		}
		String_textMsg = {
			"msgtype": "text",
			"text": {"content": message},
			"at": {
				"atMobiles": [
					"13800138000"
				]
			}
		}
		if len(name_list) > 0:
			pass
		# String_textMsg["at"]["atMobiles"] = []
		# for x in range(len(name_list)):
		#     String_textMsg["at"]["atMobiles"].append(QA_mobiles[name_list[x]])
		else:
			del String_textMsg["at"]
		String_textMsg = json.dumps(String_textMsg)
		res = requests.post(url, data=String_textMsg, headers=HEADERS)
		time.sleep(5)
		print(res.text)

	@property
	def get_system(self):
		import platform
		return platform.system().lower()

	def get_time(self):
		ct = time.time()
		local_time = time.localtime(ct)
		data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
		data_secs = int((ct - int(ct)) * 1000)
		return "{}:{}".format(data_head, data_secs)


if __name__ == "__main__":
	test = CommonBase()
	print(test.root_path)
