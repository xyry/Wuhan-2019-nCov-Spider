#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    : 2020/1/30 16:40
# @Author  : YPL
# @FileName: get_2019-nCov_data.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import requests
import bs4
import time
import re
def gethtml(url,headers):
    response=requests.get(url,headers=headers)
    try:
        if response.status_code==200:
            # print('抓取网页成功：',len(response.text))
            response.encoding='utf-8'
            return response.text
    except BaseException as e:
        print('抓取出现错误：',e)

if __name__ =='__main__':
    start=time.time()
    url='https://3g.dxy.cn/newh5/view/pneumonia'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    html=gethtml(url,headers)
    soup = BeautifulSoup(html, 'html.parser')
    data = soup.find_all(id='getStatisticsService')
    # s = str(data).split('{')[2].split('}')[0][322:400]
    s = str(data).split('{')[2].split('}')[0][322:500]
	
    list_n = re.findall('\d{1,10}', s)
    # print(list_n)
    # print(str(data))
    s1="确诊人数：" + str(list_n[0]) + "   疑似人数：" + str(list_n[1]) + "   治愈人数：" + str(list_n[2]) + "   死亡人数：" + str(list_n[3])
    s2='数据来源：' + str(url) + " 当前时间：" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # print("确诊人数：", list_n[0], " 疑似人数：", list_n[1], " 治愈人数：", list_n[2], " 死亡人数：", list_n[3])
    # print('数据来源', url, " 当前时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # print(str(s1))
    # print(str(s2))
    with open('/mnt/tecmint/ypl_file/cron_job/Wuhan_2019-nCoV.txt','a') as f:
        f.write(str(s2) + '\n')
        f.write(str(s1)+'\n')
        f.write('\n')
    with open('/mnt/tecmint/ypl_file/cron_job/Wuhan_2019-nCoV_RawData.txt','a') as f:
        f.write(str(list_n)+'   '+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+'\n')

    # end=time.time()

    # print('耗时:',end-start)