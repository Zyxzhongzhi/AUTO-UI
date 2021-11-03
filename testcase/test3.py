#coding=utf-8
'''
time:2020/8/20 16:58
'''
from selenium import webdriver
import unittest
from time import sleep

@unittest.skip
class Yuemi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        # self.driver.implicitly_wait(10)
        # self.driver.get('http://testyuemi.ziyuenet.com.cn:8282')
        cls.driver.get('http://47.102.151.167/login')
        sleep(2)
        cls.driver.find_element_by_class_name('teacher').click()      #教师端
        cls.driver.find_element_by_xpath('//*[@id="login-item"]/div[2]/div[1]/input').send_keys('teacher001')        #账号
        cls.driver.find_element_by_xpath('//*[@id="login-item"]/div[2]/div[2]/input').send_keys('teacher2020')       #密码
        sleep(2)
        cls.driver.find_element_by_xpath('//*[@id="login-item"]/div[2]/div[4]/span').click()          #登录
        sleep(2)

    def test001(self):
        driver = self.driver
        driver.find_element_by_class_name('interaction-name').click()        #课堂互动
        sleep(2)
        driver.find_element_by_class_name('call-index').click()              #点名
        sleep(2)
        driver.find_element_by_class_name('interact-answer-btn').click()     #开始抢答
        # sleep(2)
        # driver.find_element_by_class_name('random-smoke').click()            #随机点名
        sleep(2)
        # driver.find_element_by_class_name('next-interact').click()           #使用抢答
        driver.find_element_by_class_name('interact-answer-btn').click()      #结束抢答
        sleep(2)
        # driver.find_element_by_class_name('interact-close').click()          #关闭

    # def test002(self):
    #     # driver = self.driver
    #     driver.find_element_by_class_name('interaction-name').click()        # 课堂互动
    #     sleep(2)
    #     driver.find_element_by_class_name('lock-screen-index').click()       #锁屏(开)
    #     # driver.find_element_by_class_name('lock-screen-index lock-screen-active').click()     #锁屏(关)
    #
    #
    # def test003(self):
    #     driver = self.driver
    #     driver.find_element_by_class_name('handwrite-index').click()                           #白板
    #     driver.find_element_by_class_name('select-background-color').click()                   #背景色
    #     driver.find_element_by_xpath('//*[@id="handWrite"]/div[2]/div/p[6]/span[1]').click()   #字色
    #     driver.find_element_by_xpath('//*[@id="handWrite"]/div[2]/div/p[7]/span[1]').click()   #线宽
    #     sleep(6)       #手动书写
    #     driver.find_element_by_class_name('recall').click()      #撤销
    #     sleep(2)
    #     driver.find_element_by_class_name('refresh').click()     #恢复
    #     driver.find_element_by_class_name('clear').click()       #清屏


    # def tearDown(self):
    #     self.driver.refresh()
    #     sleep(2)
        # self.assertEqual([], self.verificationErrors)

    @classmethod
    def tearDownClass(cls):
    # def tearDown(self):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()