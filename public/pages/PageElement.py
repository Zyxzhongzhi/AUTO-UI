#coding=utf-8
'''
time:2020/9/10 13:12
'''

class PageElement:

    #登录元素定位
    userName = ('xpath','//*[@class="cneter-box"]/div[1]/input')
    passWord = ('xpath','//*[@class="cneter-box"]/div[2]/input')
    login = ('class','login')
    # lesson = ('class','button')
    myyuemi = ('xpath','//*[@id="app"]/div/div[1]/div/div[3]/div[1]')
    # pingtai_resource = ('class','pingtai')
    # pingtai_resource = ('xpath','//*[@class="resource-center"]/div[1]/div[2]/div[1]/div[2]/div[1]')
    pingtai_resource = ('xpath', '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]')
    # #回到首页
    # index = ('xpath','//*[@id="mn_forum"]/a')

