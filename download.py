# _*_ coding: utf-8 _*_
# __author__ = 'herrylee'

import urllib.request
import os
import socket
import requests
socket.setdefaulttimeout(60)
def download(url, name):
    try:
        conn = urllib.request.urlopen(url)
        f = open(name, 'wb')  #wb以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
        f.write(conn.read())
        f.close()
        print('Pic Saved!')
    except:
        download(url,name)
keys= ""
fp = open("C:\\Users\\Administrator\\Desktop\\2.csv","r",encoding='utf-8')#以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。修改你的文件地址
for line in fp.readlines():
     print(line)
     jin = line.split(',')[0].strip()
     wei = line.split(',')[1].strip()
    # headings = line.split(',')[2].strip()
     path = "D:\\streetview"+ jin + "_" + wei  #修改到你的地址
     isExists = os.path.exists(path)
     if not isExists:
        os.makedirs(path)
     else:
        pass
     start_heading = 0
     for j in range(6):
         headings = (start_heading + j * 60)
         name = path + '/' +str(jin) + "_" + str(wei) + "_" + str(headings) + ".jpg"
         url = "https://apis.map.qq.com/ws/streetview/v1/image?size=512x400&location=" + str(wei) + "," + str(jin) + "&heading=" +str(headings) + "&pitch=0" + '&key=填你的KEY'
         print(name)
         print(url)
         if os.path.isfile(name):
              print (name + 'had exited')
         else:
              download(url,name)

fp.close()
