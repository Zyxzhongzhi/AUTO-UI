#coding=utf-8
'''
time:2020/8/13 11:28
'''
from selenium import webdriver
import unittest
from time import sleep
from public.utils.ReadConfigIni import ReadConfigIni
from public.utils.ReadConfigIni import *

read= ReadConfigIni(os.path.join(config,'config.ini'))
url = read.get_ini_data('env','url')

class BasePage(unittest.TestCase):

    @classmethod
    def set_driver(cls,driver):
        cls.driver = driver

    @classmethod
    def get_driver(cls):
        return cls.driver

    #封装元素定位
    @classmethod
    def find_element(cls,element):
        type = element[0]
        value = element[1]
        if type == 'id':
            elem = cls.driver.find_element_by_id(value)
        elif type == 'class':
            elem = cls.driver.find_element_by_class_name(value)
        elif type == 'xpath':
            elem = cls.driver.find_element_by_xpath(value)
        else:
            raise NameError('please input correct params')
        return elem

    @classmethod
    def send_keys(cls,elem,text):
        return elem.send_keys(text)

    @classmethod
    def click(cls,elem):
        elem.click

    @classmethod
    def get_text(cls,elem):
        return BasePage.find_element(elem).text

    # @classmethod
    # def implicitlt_wait(cls):
    #

    @classmethod
    def login(cls):
        sleep(3)
        cls.driver.find_element_by_xpath('//*[@class="cneter-box"]/div[1]/input').send_keys('zhengyuxia')
        cls.driver.find_element_by_xpath('//*[@class="cneter-box"]/div[2]/input').send_keys('js123456')
        sleep(4)
        cls.driver.find_element_by_class_name('login').click()
        sleep(3)
        return cls.driver


if __name__ == '__main__':
    b = BasePage()
    baidu_input = ('id', 'kw')
    b.find_element(baidu_input)



