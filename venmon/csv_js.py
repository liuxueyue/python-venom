# from common.BeautifulReport import BeautifulReport
from common.common_base import CommonBase
from common.war.csv_to_json import Convert
import unittest
import os
import shutil
import subprocess
import argparse
import re
import time
import csv


class StartVenom(CommonBase):
    def __init__(self,**kwargs):
        super().__init__()
        self.args = kwargs
        self.venom_project = self.args['project'] #venom测试项目
        self.config = {'venom': {'FRAMEWORK_ROOT': 'G:\\git_python\\venmon', 'JSON_PATH': 'G:\\git_python\\venmon\\temp_json', 'CONFIG_PATH': 'G:\\git_python\\venmon\\temp_csv', 'CASE_ROOT': 'G:\\git_python\\venmon\\config_case'}, 'war': {'PROJECT_NAME': 'war', 'SVN_INFO': 'svn://new.svn.playcrab-inc.com/war/svn', 'BRANCH': 'war_online', 'CASE': 'war', 'CSV_SPECIAL': 'GB18030', 'CONFIG_SPECIAL': 'csv', 'DING_TOKEN': ['0bfca36866e72940a0f6cba4c9b91b9a5d9a69d6bb49de19abf4e8a2d0434147', 'ac9d671d9c281f4c2baaabd2d49edd4a22a2d68c022e2a2b37956f96bf2b8261']}, 'mars': {'PROJECT_NAME': 'mars', 'SVN_INFO': 'svn://new.svn.playcrab-inc.com/war-europe/svn', 'BRANCH': 'war_online', 'CASE': 'mars', 'CSV_SPECIAL': 'utf-8', 'CONFIG_SPECIAL': 'csv', 'DING_TOKEN': ['0bfca36866e72940a0f6cba4c9b91b9a5d9a69d6bb49de19abf4e8a2d0434147', 'ac9d671d9c281f4c2baaabd2d49edd4a22a2d68c022e2a2b37956f96bf2b8261']}}
         #venom全配置文件
        self.venom_config = self.config["venom"] #venom配置文件
        self.project_venom = self.config[self.venom_project] #venom项目配置文件
        self.case_path = f"{self.venom_config['CASE_ROOT']}/{self.project_venom['CASE']}"
        self.war = [
            "mars",
            "war"
        ]

    def prepare_check(self):
        folder = self.args['venom_name']
        if not self.args['debug']:
            if os.path.exists(self.venom_config["JSON_PATH"]):
                shutil.rmtree(self.venom_config["JSON_PATH"])
            if os.path.exists(self.venom_config["CONFIG_PATH"]):
                shutil.rmtree(self.venom_config["CONFIG_PATH"])
            os.mkdir(self.venom_config["CONFIG_PATH"])

            svn_cmd = f"svn checkout {self.project_venom['SVN_INFO']}/{folder}/{self.project_venom['CONFIG_SPECIAL']}"
            svn = subprocess.Popen(svn_cmd,
                                   shell=True,
                                   cwd=f"{self.venom_config['CONFIG_PATH']}")
            svn.wait()


        svn_info = subprocess.Popen(' svn info | grep "Last Changed Rev\:\|^最后修改的版本\:"',
                               shell=True,
                               cwd=f"{self.venom_config['CONFIG_PATH']}/{self.project_venom['CONFIG_SPECIAL']}",
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        (out, err) = svn_info.communicate()
        svn_path = f"{self.project_venom['SVN_INFO']}/{folder}"
        # version = re.sub("\D", "", str(out).replace("\\n","").replace(" ",""))
        version = str(out).split(":")[-1].replace("\n", "")  # 谁没事把服务器svn给升级了。。。
        return svn_path,version

venom = StartVenom(**{'project': 'war', 'file_name': 'ALL', 'venom_name': 'configCsv', 'report_name': 'debug_report', 'debug': False, 'similarity': 0.8})
svn_path,version = venom.prepare_check()
print(svn_path, version)