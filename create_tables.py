# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:42:19 2018

@author: mouhamed amine chalbi
"""

import sqlite3

connection= sqlite3.connect('data.db')
cursor=connection.cursor()

create_table="CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(create_table)
print("users table created")
create_table="CREATE TABLE IF NOT EXISTS trips (id INTEGER PRIMARY KEY,deperture_station text,arrival_station text,price INTEGER)"
cursor.execute(create_table)
print("trips table created")

user1=(1,'mac','1234')
insert_query="INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user1)
print("user mac created")

user1=(2,'fawzi','12345')
cursor.execute(insert_query,user1)
print("user fawzi created")

trip=(1,'tunis','medenine',23)
insert_query="INSERT INTO trips VALUES (?,?,?,?)"
cursor.execute(insert_query,trip)
print("trip tunis-medenine created")

trip=(2,'gafsa','tunis',20)
insert_query="INSERT INTO trips VALUES (?,?,?,?)"
cursor.execute(insert_query,trip)
print("trip tunis-medenine created")

trip=(3,'chicha land','anywhere',0)
insert_query="INSERT INTO trips VALUES (?,?,?,?)"
cursor.execute(insert_query,trip)
print("trip tunis-medenine created")



connection.commit()
connection.close()                                               
