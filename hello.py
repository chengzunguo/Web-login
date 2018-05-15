#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Marte
# @Date:   2018-05-09 19:46:51
# @Last Modified by:   Marte
# @Last Modified time: 2018-05-12 15:09:22


print("hello world")

# C:\Users\Administrator\Desktop\

# 'cd C:\Users\Administrator\Desktop\mywebproject python manage.py runserver'

# def Mongod_bat(path):
#     with open("mywebproject.bat","w",encoding="ANSI") as file:

#         file.write("""@echo off
# cd "%s"
# python manage.py runserver 0.0.0.0:8000
# pause"""%path)


def Mongod_bat(path):
    with open("openRedis.bat","w",encoding="ANSI") as file:

        file.write("""@echo off
cd "%s"
d:
cd redis
redis-server.exe redis.windows.conf

pause"""%path)

Mongod_bat(r'C:\Users\Administrator\Desktop\mywebproject')
# # 
#

# import pymongo 

# conn = pymongo.MongoClient('localhost',27017)

# db = conn.mydb

# data = db.student.find()

# print(type(data))

# for i in data:
#     print(i)
#     print(type(i))



# import redis

# client  = redis.StrictRedis(
#     # host = 'localhost',
#     # port = 6379,
#     db=1,
#     password = '123400'
#     )

# print(client.get('name'))

# print(client.hgetall('person'))


# client.hmset("dog",{"name":"中华田园犬","age":10})

# print(client.hgetall('dog'))

# line = '中华田园犬'
# lineB = line.encode('utf-8')
# lineS = lineB.decode('utf-8')

# print(lineS)
# print(type(lineS))





