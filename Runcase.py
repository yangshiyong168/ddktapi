#coding=utf-8
import  os
from NewWorld.Public.HTMLTestRunner import *
#定义路径case目录
casepath=os.getcwd()+"\\Testcase"
#报告存放路径
reportpath=os.getcwd()+"\\Report\\"
print casepath
#搜索用例到容器
suit=unittest.defaultTestLoader.discover(casepath,pattern='*.py')
print suit
#写报告
reportname=reportpath+'Selenium_'+time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())+'.html'
print reportname
fp=open(reportname,"wb")
HTMLTestRunner(stream=fp,title=u'NewWorld自动化测试报告',description=u'描述').run(suit)
fp.close()
