# coding = utf-8
'''
time:2021/6/30 15:48
'''
from selenium import webdriver
from public.pages.BasePage import BasePage
from public.pages.PageElement import PageElement as p
from public.utils.ReadConfigIni import ReadConfigIni
from public.utils.ReadConfigIni import *
from config.path import *
from time import sleep
import unittest
import time
import os

read = ReadConfigIni(os.path.join(config, 'config.ini'))
url = read.get_ini_data('env', 'url')
username = read.get_ini_data('env', 'username')
password = read.get_ini_data('env', 'password')

# @unittest.skip
class Yuemi_resource(BasePage):

    @classmethod
    def setUpClass(cls):
        # driver = webdriver.Chrome()
        BasePage.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test002_resource(self):
        # driver = BasePage.get_driver()  # 拿到谷歌浏览器对象
        # driver.get(url)
        # BasePage.login()
        sleep(4)
        # 5.平台资源
        elem = BasePage.find_element(p.pingtai_resource)
        BasePage.click(elem)
        sleep(3)

if __name__ == '__main__':
    unittest.main()