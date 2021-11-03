#coding=utf-8
from selenium import webdriver
from public.pages.BasePage import BasePage
from public.pages.BasePage import *
from public.pages.PageElement import PageElement as p
from public.utils.ReadConfigIni import ReadConfigIni
from public.utils.ReadConfigIni import *
from config.path import *
from time import sleep
import unittest
import time
import os
from selenium.webdriver.support.ui import WebDriverWait

read= ReadConfigIni(os.path.join(config,'config.ini'))
url = read.get_ini_data('env','url')
username = read.get_ini_data('env','username')
password = read.get_ini_data('env','password')
print(url)
print(username)
print(password)
# @unittest.skip
class Yuemi(BasePage):

    @classmethod
    def setUpClass(cls):
        driver = webdriver.Chrome()
        BasePage.set_driver(driver)
        driver = BasePage.get_driver()  # 拿到谷歌浏览器对象
        driver.get(url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # BasePage.go_home(p.index)

    def test001_login(self):
        sleep(3)
        # 1.输入账号
        elem = BasePage.find_element(p.userName)
        BasePage.send_keys(elem,username)
        # 2.输入密码
        elem = BasePage.find_element(p.passWord)
        BasePage.send_keys(elem,password)
        sleep(4)
        #3.点击登录
        elem = BasePage.find_element(p.login)
        BasePage.click(elem)
        # sleep(4)
        # 4.进行断言
        # WebDriverWait(10,1).until(p.myyuemi)
        value = BasePage.get_text(p.myyuemi)
        print(value)
        assert value == u'我的越米'
        sleep(3)
# if __name__ == '__main__':
#     unittest.main()
    # testunit = unittest.TestSuite()#初始化测试用例集合对象，构建测试套件
    # # testunit.addTest(Baidu("test_baidu_search"))#把测试用例加入到测试用力集合中去，将用例加入到检测套件中
    # fp = open('./result.html','wb')#定义测试报告存放路径
    # runner = HTMLTestRunner(stream=fp,title='越米云助教测试报告',description='用例执行情况')#定义测试报告
    # runner.run(testunit)#执行测试用例
    # fp.close()

