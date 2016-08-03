# -*- coding:utf-8 -*-


import urllib
import urllib.request
import re
from collections import deque
import time
class pa():

    def __init__(self):
        self.siteURL = "http://news.dbanotes.net/"
        self.queue = deque()#list采用hash算法，pop和append方法比较耗时，使用deque性能较好
        self.visited = set()
        self.queue.append(self.siteURL)

    def getPage(self):
        index = 0
        while self.queue:
            url = self.queue.popleft()  #抛出队首元素
            self.visited |= {url}   #添加抛出元素到已抓取列表，防止重复抓取
            print("已经抓取了"+str(index)+"条数据，正在抓取"+url)
            index += 1
            try:
                urlop = urllib.request.urlopen(url,timeout=2)     #http.client.HTTPResponse对象
                if "html" not in urlop.getheader('Content-type'):
                    continue
                data = urlop.read().decode('utf-8')     #页面数据

            except:
                continue

            link = re.compile('href=\"(.+?)\"')     #用正则判断抓取的链接
            for x in link.findall(data):
                if 'http' in x and x not in self.visited:
                    self.queue.append(x)
                    print("加入队列--->"+x)

spider = pa()
spider.getPage()

print("已全部抓取完毕")