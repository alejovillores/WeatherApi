# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:10:56 2021

@author: alejo
"""
import api
import data_weather_manager

class Menu:
    
    def __init__(self):
        self.key = '0765a352299af83f9a0dcb84b1ac1c59'
        self.api =api.WearherApi(key)