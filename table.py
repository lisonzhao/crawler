
from bs4 import BeautifulSoup
import requests
import csv
import bs4
import os
# 检查url地址
def check_link(url):
    try:

        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法链接服务器！！！')


# 爬取资源
def get_contents(ulist, rurl):
    soup = BeautifulSoup(rurl, 'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)
def main():
    urli = []
    list = [

300750,

]
    #szcn
    #szsme
    #szmb
    #shmb
    for i in list:
        a = ("%06d" % i)
        url = "http://www.cninfo.com.cn/information/brief/szcn"+str(a) +".html"
        rs = check_link(url)
        urli=[]
        get_contents(urli, rs)
        print(a)

        with open("F:/爬取数据/"+str(a) +".SZ/公司概况"+str(a) +".txt", 'w', newline='', encoding='utf-8') as f:

            f.write('公司概况'+'\r\n')
            for i in range(len(urli) - 1):
                stra =str(i + 1).strip()
                strb =str(urli[i + 1][1])[:-1].strip()
                strc =str(urli[i + 1][3]).strip()
                f.write(stra + '#' + strb + '#' +strc+ '\r\n')

main()