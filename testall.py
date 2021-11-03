#coding=utf-8

from config import path
from public.utils import HTMLTestRunner3
from public.utils import mail
# from public.utils import HTMLTestRunnerCN
import time
import unittest

def auto_all():

    start_dir = r'C:\Users\admin\Desktop\08041/testcase'
    discover = unittest.defaultTestLoader.discover(start_dir=start_dir,pattern='te*.py')

    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    # print now

    filename =path.report+'\\'+str(now)+'_ui.html'
    # print filename

    f = open(filename,'wb')
    runner = HTMLTestRunner3.HTMLTestRunner(
        stream=f,
        title=u'越米云自动化测试报告',
        description=u'详细测试用例结果'
      )

    runner.run(discover)
    f.close()



if __name__ == '__main__':
    auto_all()
