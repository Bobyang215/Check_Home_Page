import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def Screenshot_home_page(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome()
    # 打开网页:
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)
     # 网页截图且保存下来，地址自己修改
    #file_address ="/Users/yangbo/Desktop/temporary/screenshots/"
    #提取域名
    url_name=url.split('.',2)[1]
    #对首页截图并保存
    driver.get_screenshot_as_file("/Users/yangbo/Desktop/temporary/screenshots/{}.png".format(url_name))
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
        # 'https://www.singleparentmatch.com',
        # 'https://www.mixdmatch.com',
        # 'https://www.asexualcupid.com',
        # 'https://www.bikerkiss.com',
        # 'https://www.agematch.com',
        # 'https://www.deafs.com',
        # 'https://www.nudistfriends.com',
        # 'https://www.bicupid.com',
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

