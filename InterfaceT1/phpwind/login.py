# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from selenium import webdriver
import time
dr = webdriver.Chrome()
dr.get("https://ssl.ptlogin2.qq.com/qqmail?pt_clientver=5569&pt_src=1&keyindex=9&Fun=clientread&ADUIN=315594984&ADSESSION=iii&ADTAG=jjj&clientuin=315594984&clientkey=00015B90EE890068FF073B771CC741B5E9A13FCE1CA5E9598B223E66E5853D431CE12AFC9830DECAD063F7196F621CE5727C5627250045AA072CCFC9FD97A47B5C83682B6FCF4917EA39413261C659D9AE7712B0FC7109B1C9F09C2D8BBF88A27B47184F0727DB222FDA8BE7143053F8&ptlang=2052&httptype=0&ADUIN=315594984&ADSESSION=1536219576&ADTAG=CLIENT.QQ.5569_Mysrv.0&ADPUBNO=26799")
print(dr.window_handles)
dr.find_element_by_id("composebtn").click()
print(dr.window_handles)
dr.switch_to_frame()
# dr.find_element_by_xpath("//*[@id=\"toAreaCtrl\"]").send_keys("1111")
# dr.find_element_by_xpath("//*[@id='u1']/a[7]").click()
# time.sleep(8)
# dr.find_element_by_xpath("//*[@id=\"pass_phoenix_btn\"]/ul/li[2]/a").click()
hon3.6.5\python.exe C:/Users/monitor/PycharmProjects/InterfaceT1/phpwind/login.py
['CDwindow-C65E4F56C06AA915AE6A0616FEC14225']
['CDwindow-C65E4F56C06AA915AE6A0616FEC14225']

Process finished with exit code 0
# allHandles = dr.window_handles
# print("当前所有窗口的句柄：" +str(allHandles))
# currentHandle = dr.current_window_handle
# print("当前窗口句柄为" +str(currentHandle))
# for allhandle in allHandles:
#     if allhandle != currentHandle:
#         dr.switch_to.window(allhandle)
# print("目前操作的句柄为："+ dr.current_window_handle)