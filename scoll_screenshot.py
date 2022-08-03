# _*_ coding:utf-8 _*_
# @Time : 2022/8/3 09:23
# @Author: Bob Yang
# @File : scoll_screenshot.py
# @Content: 只开启了8个主站的分屏截图
import datetime
import math
import os
import ssl
import time

import Image
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def Screenshot_home_page(url):
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    requests.packages.urllib3.disable_warnings()
    # 关闭ssl认证
    ssl._create_default_https_context = ssl._create_unverified_context  # 如果不添加这两行，下一行报错
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        'authorization': "Basic c3VwcG9ydDptczM1Nw=="  # 测试站需要添加这个认证信息
    }
    driver = webdriver.Chrome()
    # 打开网页:
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
    # 提取域名
    url_name = url.split('.', 2)[1]

    #关闭底部cookie 协议弹窗
    #driver.find_element(By.CLASS_NAME,"cc_b_ok").click()
    start_higth = 0   #默认起始高端为0
    sc_hight=800  #设置截图默认高度，可根据屏幕实际情况，修改参数大小
    el = driver.find_element(By.XPATH, "/html/body")
    try:
        #长页面进行分页截图
        if el.size["height"] > sc_hight:
            #long_sc(el,driver)
            count =math.ceil(el.size["height"] / sc_hight) #计算需要滑动几次
            for i in range (0,count):
                js="scrollTo(0,%s) "%(start_higth + i * sc_hight) #滑动翻页
                driver.execute_script(js)  #执行js脚本
                time.sleep(1)
                # 对截图并保存
                # # #创建临时保存图片目录
                # path = r"/Users/yangbo/Desktop/temporary/screenshots/{}".format(url_name)
                # os.mkdir(path)
                driver.get_screenshot_as_file("/Users/yangbo/Desktop/temporary/screenshots/{}{}.png".format(url_name,i))
        else:
            # 对截图并保存
            driver.get_screenshot_as_file("/Users/yangbo/Desktop/temporary/screenshots/{}.png".format(url_name))
    except Exception as e:
        print(e)
    # 关闭浏览器
    driver.quit()


if __name__ == '__main__':
    # 配置需要检测的url，有更新就直接添加，不需要检测的直接注释或删掉
    url = {
        #"https://lf.masonvips.com",
        #"https://www.masonvips.com",
        'https://www.seniormatch.com',
        'https://www.pmeet.com',
        'https://www.sugardaddymeet.com',
        'https://www.positivesingles.com',
        'https://www.millionairematch.com',
        'https://www.olderwomendating.com',
        'https://www.mpwh.com',
        'https://www.bicupid.com',
        # 'https://www.singleparentmatch.com',
        # 'https://www.mixdmatch.com',
        # 'https://www.asexualcupid.com',
        # 'https://www.bikerkiss.com',
        # 'https://www.agematch.com',
        # 'https://www.deafs.com',
        # 'https://www.nudistfriends.com',
        # 'https://www.ldate.com',
        # 'https://www.FlirtyMeet.com',
        # 'https://www.interracialmatch.com',
        # 'https://www.youngerwomendating.com',
        # 'https://www.pozmatch.com',
        # 'https://www.lseeker.com',
        # 'https://www.gkiss.com',
        # 'https://www.agelove.com',
        # 'https://www.gothicmatch.com',
        # 'https://www.FwbFlirt.com',
        # 'https://www.militaryfriends.com',
        # 'https://www.equestriancupid.com',
        # 'https://www.largefriends.com',
        # 'https://www.matchcougar.com',
        # 'https://www.tallfriends.com',
    }
    # 调用检测方法 Screenshot_Home_Page()
    #print(datetime.datetime.now())
    for u in url:
        Screenshot_home_page(u)
    print("There are %d sites have checked completed!" % len(url))

   # print(datetime.datetime.now())

