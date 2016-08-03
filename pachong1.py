# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import http.cookiejar
import urllib.request
from collections import deque
import re
def go(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key,value in head.items():
        element = (key,value)
        header.append(element)
    opener.addheaders = header
    return opener

def save(data,title):
    if(not title):
        return
    save_path="d:\\py\\txt\\"+str(title)+".html"
    f_obj = open(save_path,'wb')
    data = data.encode(encoding='utf-8')
    f_obj.write(data)
    f_obj.close()

def getPage(op,url):
    index = 0
    queue = deque()
    visited = set()
    queue.append(url)

    while queue:
        urll = queue.popleft()
        visited |= {urll}
        print("已经抓取了" + str(index) + "条数据，正在抓取" + urll)
        index += 1
        try:
            open = op.open(urll)
            if 'html' not in open.getheader('Content-type'):
                continue
            data = open.read().decode('utf-8')

            bs = BeautifulSoup(data)
            if(len(bs.find_all(id='viewpost1_TitleUrl')) > 0):
                title = bs.find_all(id='viewpost1_TitleUrl')[0].string
                save(data, title)
                print(title)
        except:
            continue
        if bs.find('div',class_='post'):
            div = bs.find('div',class_='post').find_all('a',class_='')
        #print(div)
        link = re.compile('href=\"(.+?)\"')
        for x in div:
            #print(x)
            if x.string != '阅读全文' and 'blogjava' in x['href'] and x not in visited:
                queue.append(x['href'])
                #print("加入队列--->" + x['href'])
                pass



op = go()
getPage(op,"http://www.blogjava.net//")
op.close()
#uop = op.open("http://news.dbanotes.net/")
#data = uop.read().decode('utf-8')
#data = data.encode(encoding='utf-8')
#print(type(data))
#save(data)
#print(data)

