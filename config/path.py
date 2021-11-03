#coding=utf-8
'''
配置所有的包的绝对路径
'''
import os

project_path = os.path.dirname(os.path.dirname(__file__))

config = os.path.join(project_path,'config')

data = os.path.join(project_path,'data')

public = os.path.join(project_path,'public')

report = os.path.join(project_path,'report')

testcase = os.path.join(project_path,'testcase')

print(config)
print(project_path)
print(report)