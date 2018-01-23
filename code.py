#! /usr/bin/env python

import os, requests, time, re, sys
from bs4 import BeautifulSoup
from datetime import datetime

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

#url = 'https://www.zhihu.com/people/jiafeili/activities'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}

def get_count(url):
   r = requests.get(url, headers = headers)
   html_doc = r.text
   soup = BeautifulSoup(html_doc,'lxml')
   sidebar = soup.find_all('div', {"class":"Profile-sideColumnItem"})
   follower = soup.find_all('div', {"class": "NumberBoard-itemInner"})
   
   num = []

   for a in sidebar:
   	temp1 = a.get_text().encode('utf-8').replace(",", "")
   	tempCount = re.findall(r'\d+', temp1)
   	if len(tempCount) == 3:
   		num = num+ tempCount

   
   textLine2 = follower[1].get_text().encode('utf-8').replace(",", "")
   textLine2 = re.findall(r'\d+',textLine2)
   num.append(textLine2[0])

   d = time.strftime("%x")
   t = time.strftime("%X")

   userName = soup.find_all('span',{'class':"ProfileHeader-name"})
   user = userName[0].get_text().encode('utf-8')

   result = [d]+ [t] + [user] + num
   resultText =  ','.join(result)   

   with open('/home/lunl/Dropbox/Python/Follower_Count/result.csv', 'a+') as f:
      print >> f, resultText
   f.close()


def get_count_mass(urllist):
   for u in urllist:
      get_count(u)

userlist = ['jiafeili','sgai','li-lei-up','fatfox10','wen-yi-fei-31','daifuku',
	'shan-yang-yue','divinites','richard-xu-25','Orzhui','xingrima','he-ming-ke',
	'jixin','drpmdb','econhistorylover','nashlew','sijichun','koukou0113',
	'zhou-hao-94','chen-zhuo-49','chenqin','zhang-jia-wei','liangbianyao','zcw-gaizhili']


urllist = ['https://www.zhihu.com/people/'+a+'/activities' for a in userlist]

get_count_mass(urllist)

