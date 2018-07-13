import requests
from selenium import webdriver
import re
from bs4 import BeautifulSoup
#下载过程
def download_docx_series(docx_links):
    for link in docx_links:
        file_name = link.split('/')[-1]
        print("Downloading file:%s" % file_name)
        r = requests.get(link, stream=True)
        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        print("%s downloaded!\n" % file_name)
    return

#list 为巨潮资讯网股票编号
list = [
        1,
    ]
for i in list:
    a = ("%06d" % i)
    url = "http://www.cninfo.com.cn/unit/list.html?w=672&s=%2Fdisclosure%2Ftzzgxxx%2Fstocks%2Fzxxx1y%2Fcninfo%2F" + str(
            a) + ".js&t=1,2"
    driver = webdriver.PhantomJS(executable_path='F:/phantomjs/bin/phantomjs.exe')  # 这个路径就是你添加到PATH的路径
    driver.get(url)
    page = driver.page_source
    # print page
    # "非贪婪匹配,re.S('.'匹配字符,包括换行符)"
    # docx_list = re.findall(r"docx$"'href=\"(.*?)\"', page,re.S)
    #用beautifulsoup获取标签内下载链接
    soup = BeautifulSoup(page, features='lxml')
    docx_links = soup.find_all('a', {'href': re.compile('.*?\.DOCX')})
    archive_url="http://www.cninfo.com.cn"
    for link in docx_links:
        docx_links = [archive_url + link['href'] ]
        download_docx_series(docx_links)
    print("All docx downloaded!")