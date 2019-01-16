# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:42:19 2018

@author: mouhamed amine chalbi
"""

import sqlite3

connection= sqlite3.connect('data.db')
cursor=connection.cursor()

create_table="CREATE TABLE IF NOT EXISTS users (idU INTEGER PRIMARY KEY ,username text,password text)"
cursor.execute(create_table)
print("users table created")
create_table="DROP TABLE IF EXISTS trips"
cursor.execute(create_table)
create_table="CREATE TABLE trips (idT INTEGER PRIMARY KEY,deperture_station text,arrival_station text,price INTEGER)"
cursor.execute(create_table)
print("trips table created")
create_table="CREATE TABLE IF NOT EXISTS reservations (idR INTEGER PRIMARY KEY,idT INTEGER,idU INTEGER,quantity INTEGER,ticket_code INTEGER)"
cursor.execute(create_table)
print("reservations table created")
create_table="CREATE TABLE IF NOT EXISTS tickets (idTK INTEGER PRIMARY KEY ,idU INTEGER,idT INTEGER, code text,FOREIGN KEY (idT) REFERENCES trips(idT))"
cursor.execute(create_table)
print("tickets table created")
# user1=(1,'mac','1234')
# insert_query="INSERT INTO users VALUES (?,?,?)"
# cursor.execute(insert_query,user1)
# print("user mac created")

# user1=(2,'fawzi','12345')
# cursor.execute(insert_query,user1)
# print("user fawzi created")

trip=('tunis','medenine',23)
insert_query="INSERT INTO trips VALUES (NULL,?,?,?)"
cursor.execute(insert_query,trip)
trip=('tunis','monastir',10)
insert_query="INSERT INTO trips VALUES (NULL,?,?,?)"
cursor.execute(insert_query,trip)
trip=('tunis','gafsa',20)
insert_query="INSERT INTO trips VALUES (NULL,?,?,?)"
cursor.execute(insert_query,trip)

print("trip tunis-medenine created")

trip=('gafsa','tunis',20)
insert_query="INSERT INTO trips VALUES (NULL,?,?,?)"
cursor.execute(insert_query,trip)
print("trip tunis-medenine created")

trip=('chicha land','anywhere',0)
insert_query="INSERT INTO trips VALUES (NULL,?,?,?)"
cursor.execute(insert_query,trip)
print("trip tunis-medenine created")



connection.commit()
connection.close()                                               
