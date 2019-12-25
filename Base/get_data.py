import os

import yaml


class GetData():
    def get_yaml_data(self,yml_name):
        """返回yaml文件所数据"""
        with open("./data" + os.sep + yml_name, encoding="utf-8") as f:
            return yaml.safe_load(f)


