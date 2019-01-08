# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:16:21 2018

@author: mouhamed amine chalbi

"""
from werkzeug.security import safe_str_cmp
from user import User


def authenticate(username,password):
    user=User.find_by_username(username)
    print('zebi zebi authentication fel zebi')
    if user and safe_str_cmp(user.password,password):
        return user
    else :
    	return { "message":"3asba triya"}
def identity(payload):
    user_id=payload['identity']
    return User.find_by_id(user_id)
