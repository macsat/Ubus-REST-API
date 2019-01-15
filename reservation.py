# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:37:13 2018

@author: mouhamed amine chalbi
"""
from random import randint
import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import current_identity,jwt_required

class Reservation(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('trip',type=str,required=True,help="this field must be filled")
    parser.add_argument('quantity',type=int,required=True,help="this field must be filled")
    @classmethod
    def find_by_id(cls, idR):
        print("calling find by id reservation")
        connection=sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM reservations WHERE idR=?"
        result=cursor.execute(query,(idR,))
        row = result.fetchone()
        if row:
            reservation = cls(*row)
        else:
            reservation = None
            
        connection.close()
        return reservation

    @jwt_required()
    def get(self):
    # Access the identity of the current user with get_jwt_identity
        user_id=dict(current_identity)["user_id"]
        if user_id:
            connection=sqlite3.connect("data.db")
            cursor=connection.cursor()
            query="SELECT * FROM tickets WHERE idU=?" #OR arrival_station LIKE=?
            result=cursor.execute(query,(user_id,))
            all_rows=result.fetchall()
            connection.close()
        if all_rows:
            print(type(all_rows))
            print(all_rows)
            return {"tickets":all_rows},200
        return {"message":"You don't have any tickets please reserve one first"},404

    @jwt_required()
    def post(self):
        data=Reservation.parser.parse_args()
        user_id=dict(current_identity)["user_id"]
       #if User.find_by_id(data["idR"]):
       #    return {"message":"username al"},401
        if user_id:
            connection=sqlite3.connect('data.db')
            code=randint(100000, 999999)  
            cursor = connection.cursor()
            query = "INSERT INTO reservations  VALUES (NULL, ?,?, ?,?)"
            cursor.execute(query,(data['trip'],user_id,data['quantity'],code))
            query = "INSERT INTO tickets  VALUES (NULL,?, ?,?)"
            cursor.execute(query,(user_id,data['trip'],code))
            connection.commit()
            connection.close()
            return {"ticket code": code}, 201
        return {"message":"reservation error try again"},400