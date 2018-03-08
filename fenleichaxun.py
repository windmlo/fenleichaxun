# -*- coding: utf-8 -*-
import urllib
import urllib2
import time
import re
import requests
ccnt = 0 # 用来计数一共开了多少个网页

headers = {
'Host': 'www2.soopat.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://www2.soopat.com/analytics/result?Sort=&View=&Columns=&Valid=&Embed=&Db=&Ids=&FolderIds=&FolderId=&ImportPatentIndex=&Filter=&SearchWord=SQRQ%3A%282016%29+DZ%3A%28%E5%8D%97%E4%BA%AC%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '207',
'Cookie': 'advu4=; patentids=; auth=ce644ADj3r5NJVn5G61upbaS0YwDNJohwXxZwcuKZerfEwXHjEH8SkHtz9vTW2dOMs9gvUPP4mE6elQGZ13fz2lINuod; suid=0B85F46AD038AB01; sunm=%C1%BD%D0%A1; advu1=; advu2=; advu3=',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1'
}

def store(city,invnuti,invention,utility,appearance):
    f = open(u"发明和实用新型申请日期3.txt", "a")
    f.write(city)
    for i in invnuti:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()

    f = open(u"发明专利申请日期3.txt", "a")
    f.write(city)
    for i in invention:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()

    f = open(u"实用新型申请日期3.txt", "a")
    f.write(city)
    for i in utility:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()

    f = open(u"外观设计申请日期3.txt", "a")
    f.write(city)
    for i in appearance:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()


def deal(city):# 函数参数city 城市名 根据城市名生成url
    global ccnt
    a = []
    b = []
    c = []
    d = []
    for i in range(2000, 2016+1):
        time.sleep(2)
        ccnt = ccnt + 1
        data = 'Category=GKRQY&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28'+str(i)+'%29+DZ%3A%28'+str(city)+'%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        testurl = 'http://www2.soopat.com/Analytics/Result'
        print i, city
        x = 0
        while x == 0:
            x, number = hurtspirit(testurl, headers, data, i)


        while len(number) < 10:
            number.append(0)
        print number
        a.append(number[2])
        b.append(number[4])
        c.append(number[6])
        d.append(number[8])
    store(city, a, b, c, d)

def hurtspirit(testurl, headers, data, i):
    try:
        number = find(testurl, headers, data, i)
    except:
        number = []
        print "mmp"
        time.sleep(5)
        return 0, number

    return 1, number



def find(testurl, headers, data, i):
    s = requests.get(testurl, headers=headers, data=data)
    #print s.text
    pip = str(i)+u'年.?\n 数量：(\d+)" />'
    pattern = re.compile(pip)
    number = re.findall(pattern, s.text)
    print number
    return number

def main():
    f = open('cities.txt', 'r')
    while 1:
        line = f.readline()
        if not line:
            break
        deal(line)
        n = f.readline()
        for i in range(int(n)):
            line = f.readline()
            deal(line)
    f.close()
    print('total pages:%d' % (ccnt))


if __name__ == '__main__':
    main()
