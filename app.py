# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 11:03:06 2018

REST api using flask

@author: mouhamed amine chalbi
"""

from flask import Flask
from flask_restful import Api,Resource
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate , identity
from user import UserRegister
from item import Item,ItemList
from reservation import Reservation
import create_tables 

app=Flask(__name__)
api=Api(app)
app.secret_key="secretkey"
jwt=JWT(app,authenticate,identity)# /auth


items=[{'name': 'tunis-medenine', 'price':23},
      {'name': 'gabes-medenine', 'price':5},
      {'name': 'sfax-medenine', 'price':10},
      {'name': 'tunis-sousse', 'price':10}
    ]

class PrivateResource(Resource):
    @jwt_required()
    def get(self):
        return dict(current_identity)
        
api.add_resource(PrivateResource,'/private')
api.add_resource(Reservation,'/reserve')
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(UserRegister,'/register')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=False)
