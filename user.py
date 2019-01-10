# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:37:13 2018

@author: mouhamed amine chalbi
"""
import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self,_id,username,password):
        self.id=_id
        self.username=username
        self.password=password
    
    @classmethod
    def find_by_username(cls,username):
        print("calling find by name")
        connection=sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        result=cursor.execute(query,(username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
            
        connection.close()
        return user
    @classmethod
    def find_by_id(cls, _id):
        print("calling find by id")
        connection=sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM users WHERE id=?"
        result=cursor.execute(query,(_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None
            
        connection.close()
        return user
    
class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help="this field must be filled")
    parser.add_argument('password',type=str,required=True,help="this field must be filled")
    def post(self):
        data=UserRegister.parser.parse_args()
        print(data)
        print(type(data))
        if User.find_by_username(data["username"]):
            return {"message":"username already exists please choose another username"},400
        connection=sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "INSERT INTO users  VALUES (NULL, ?, ?)"
        cursor.execute(query,(data['username'],data['password']))
        connection.commit()
        connection.close()
        return {"message": "user created successfully"}, 201
