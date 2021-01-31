#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : wuyinan02@playcrab.com
# @Desc    :
from common.common_base import CommonBase
from common.common_load import CommonLoad
from common.singleton import Singleton

class ReleaseBugData(CommonBase,metaclass=Singleton):
    def __init__(self):
        super().__init__()

    def get_diagramId_cost(self):
        test_data = []
        config = CommonLoad("battleDiagram").get_all_data()
        print(config)
        for k,v in config.items():
            if v.get("diagramId") and v.get("ecpend2"):
                diagramId = int(v["diagramId"])
                if 1001 <= diagramId <= 3024 or  4001 <= diagramId <= 4030:
                    test_data.append(self.copy_key_to_value(k,v))
        return test_data


if __name__ == "__main__":
    test = ReleaseBugData()
    print(test.get_diagramId_cost())