#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import MySQLdb as mdb
import sys
con = mdb.connect('localhost','root','qwerty','test')
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS \
        Users(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")
    cur.execute("INSERT INTO Users(Name) VALUES('Richard shen')")
    cur.execute("INSERT INTO Users(Name) VALUES('Zhang san')")
    cur.execute("INSERT INTO Users(Name) VALUES('Li si')")
    cur.execute("INSERT INTO Users(Name) VALUES('Wang dongdong ')")