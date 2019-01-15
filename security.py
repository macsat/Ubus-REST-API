# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:16:21 2018

@author: mouhamed amine chalbi

"""
from werkzeug.security import safe_str_cmp
from user import User
from passlib.hash import pbkdf2_sha256

def authenticate(username,password):
    user=User.find_by_username(username)
    print("//////////////////////////////")
    print('Authenticating user : ')
    print(username)
    print('//////////////////////////////')
    if user and pbkdf2_sha256.verify(password,user.password):
    	return user
    #if user and safe_str_cmp(user.password,password):
    #	return user

# def identity(payload):
#     user_id=payload['identity']
#     return User.find_by_id(user_id)

def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}