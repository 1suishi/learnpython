#!/usr/bin/env python
import mysql.connector
conn = mysql.connector.connect(user='root', password='qwerty',database='test', use_unicode=True)
cursor = conn.cursor()
def test():
	cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
	cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
	cursor.rowcount
	conn.commit()
	cursor.close()
	conn.close()

if __name__ == "__main__":
	test()
