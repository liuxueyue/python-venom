#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.BeautifulReport import BeautifulReport
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
        self.config = self.load_file(f"{self.root_path}/local_config.yaml") #venom全配置文件
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


    def convert_json(self):
        if self.venom_project in self.war and not self.args['debug']:
            convert = Convert(self.venom_project,self.config)
            convert.convert()
        else:
            pass


    def creat_tmp_folder(self):
        if os.path.exists(f"{self.venom_config['CASE_ROOT']}/temp_case"):
            shutil.rmtree(f"{self.venom_config['CASE_ROOT']}/temp_case")
        os.mkdir(f"{self.venom_config['CASE_ROOT']}/temp_case")
        return f"{self.venom_config['CASE_ROOT']}/temp_case"


    def screen_case(self,name):
        import difflib
        _ = []
        case_name = self.args['file_name'].replace("'", "").replace('"', "").replace(" ", "").replace("，", ",").split(",")
        for x in case_name:
            if difflib.SequenceMatcher(None, name, x).quick_ratio() > self.args['similarity'] or x in name:
                return True
        return False


    def mv_case(self):
        temp_case_path = self.creat_tmp_folder()
        for root,dirs,files in os.walk(self.case_path):
            for file in files:
                name,end = os.path.splitext(file)
                if end == ".py" and name != "__init__" and self.screen_case(name):
                    shutil.copyfile(os.path.join(root,file),os.path.join(temp_case_path,file))
        shutil.copyfile(f"{self.case_path}/__init__.py",f"{self.venom_config['CASE_ROOT']}/temp_case/__init__.py")
        self.case_path = f"{self.venom_config['CASE_ROOT']}/temp_case"


    def creat_test(self):
        test_suit = unittest.TestSuite()
        def custom_case(obj):
            for index, case in enumerate(obj._tests):
                if isinstance(case, unittest.suite.TestSuite):
                    custom_case(case)
                else:
                    if self.args["case"] in str(case):
                        test_suit.addTest(case)
            return test_suit

        if self.args['file_name'] != "ALL":
            self.mv_case()
            print(f"self.case_path === {self.case_path}")
        case = unittest.defaultTestLoader.discover(self.case_path,pattern="*.py")
        if self.args["case"] != "False" and self.args['file_name'] != "ALL":
            case = custom_case(case)
        return case


    def creat_report(self,report_data):
        if self.get_system != 'linux':
            return
        server_path = "/data/venom_report"
        #server_path = "/Users/playcrab/Documents/venom/report"

        html_path = f"{server_path}/index.html"
        csv_path = f"{server_path}/index.csv"

        first_row = [["Data", "CreatTime", "Reports"]]
        if os.path.exists(html_path):
            os.remove(html_path)

        if not os.path.exists(csv_path):
            with open(csv_path, "w", encoding='utf-8', newline='') as csv_data:
                csv_write = csv.writer(csv_data, dialect='excel')
                for key in first_row:
                    csv_write.writerow(key)

        with open(csv_path, "a", encoding='utf-8', newline='') as csv_data:
            writer = csv.writer(csv_data)
            writer.writerow([report_data, self.get_time(), '<a href="{}/index.html">查看结果</a>'.format(report_data)])

        cmd = subprocess.Popen(f"/usr/local/bin/csvtotable {csv_path} {html_path}", shell=True)
        #cmd = subprocess.Popen(f"csvtotable {csv_path} {html_path}", shell=True)
        cmd.wait()


    def __call__(self, svn_path, version):
        report_path = f'{self.venom_config["FRAMEWORK_ROOT"]}/report/{self.args["report_name"]}/'
        case = self.creat_test()
        # print(case)
        start_test = BeautifulReport(case)
        if not os.path.exists(report_path):
            os.makedirs(report_path)

        if self.args['debug']:
            report_name = "debug"
        else:
            report_name = f'report/{self.args["report_name"]}/index.html'

        print(report_name)
        start_test.report(filename=report_name,description=f"{self.args['project']} -- {self.args['venom_name']} -- {version} 测试报告")
        self.creat_report(self.args["report_name"])
        time.sleep(2)

        if "temp_case" in self.case_path:
            shutil.rmtree(self.case_path)

        if self.get_system == 'linux':
            for token in self.project_venom["DING_TOKEN"]:
                self.message(token, f"本次测试{self.args['project']}项目\n \
                序列:{self.args['venom_name']}\n \
                svn地址:{svn_path}\n \
                svn版本: {version}\n \
                测试报告地址: http://10.2.24.28:5678/{self.args['report_name']}/index.html")
                print(token)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--project", help="\n项目代号", type=str,default="war")
    parser.add_argument("-f", "--file_name", help="\n要测试的用例名", type=str, default="ALL")
    parser.add_argument("-v","--venom_name",help="venom key",default="configCsv")
    parser.add_argument("-r","--report_name", help="测试报告文件夹名", default="debug_report")
    parser.add_argument("-d","--debug",help="调试模式",action="store_true")
    parser.add_argument("-s", "--similarity", help="相似度", type=float,default=0.8)
    parser.add_argument("-c", "--case", help="指定用例中的测试方法", type=str, default="False")
    # parser.add_argument('-t',"--test", nargs="+")
    args = parser.parse_args()
    args_dic = vars(args)
    print("="*50)
    print(args)
    print(args_dic)
    print("=" * 50)

    venom = StartVenom(**args_dic)
    svn_path,version = venom.prepare_check()
    venom.convert_json()
    start = time.time()
    venom(svn_path=svn_path,version=version)
    print(time.time()-start)
