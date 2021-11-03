#coding=utf-8
'''
time:2020/8/21 17:10
'''
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://172.168.70.195:9800')
sleep(2)
driver.find_element_by_xpath('//*[@class="cneter-box"]/div[1]/input').send_keys('zhengyuxia')
driver.find_element_by_xpath('//*[@class="cneter-box"]/div[2]/input').send_keys('js123456')
sleep(4)
driver.find_element_by_class_name('login').click()
sleep(3)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]').click()
# sleep(2)
value = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[3]/div[1]').text
print(value)
assert value == u'我的越米'