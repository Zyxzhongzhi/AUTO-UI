#coding=utf-8
'''
time:2020/9/10 13:44
'''
from configparser import ConfigParser
from config.path import config

import os
class ReadConfigIni:
    def __init__(self, filename):
        self.cf = ConfigParser()  # 创建ConfigParser类的对象
        self.cf.read(filename)

    def get_ini_data(self, section, option):
        '''或者ini后缀结尾的文件内容'''
        value = self.cf.get(section, option)
        return value


if __name__ == '__main__':
    r = ReadConfigIni(os.path.join(config, 'config.ini'))
    print(r.get_ini_data('env', 'url'))