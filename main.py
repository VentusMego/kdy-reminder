# -*- coding: utf-8 -*-
import requests

from datetime import datetime
import csv
import os
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import lxml.html
import re
from bs4 import BeautifulSoup
from selenium import webdriver

# webs 可以放每一个设备活动二维码解析的网址，该网址对于设备-账号是固定的
webs = ['']
# alert_mails 预定义推送邮箱，尚未实装
alert_mails = [
        'meigo@meigo.org',
        '111'
]
#我，sy, 夺, 喵

# 更改UA破解访问限制
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override","Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1")

driver = webdriver.Firefox(profile)
driver.set_page_load_timeout(10)
driver.get(webs[0])
time.sleep(10)
html = driver.page_source # 跑出来的网页是完全的html，需要从这个文本化html抓数据
print(html)
print('以上是html')
htmlregex = re.compile(r'&nbsp;&nbsp;<span>(.*?)</span>', re.I)         # 识别计数器显示内容，需要修改
htmlregex1 = re.compile(r'<span>(.*?)</span>', re.I)
z = htmlregex1.findall(html)
print(type(z))
print('咩')
print(z)

driver.get(webs[1])
time.sleep(10)
html = driver.page_source
z = htmlregex1.findall(html)
print('sy')
print(z)

driver.get(webs[2])
time.sleep(10)
html = driver.page_source
z = htmlregex1.findall(html)
print('夺')
print(z)

driver.get(webs[3])
time.sleep(10)
html = driver.page_source
z = htmlregex1.findall(html)
print('喵')
print(z)
#bsoup = BeautifulSoup(html, "lxml")
#informations = bsoup.find_all("")
#print(informations)
#input_a = driver.find_element_by_xpath(xpath=u'//p[3]/span')
#print(input_a)
driver.close()
