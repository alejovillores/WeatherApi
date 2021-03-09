# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:51:10 2021

@author: alejo
"""

class DataWeatherManager:
    
    def __init__(self,data):
        self.data = data
    
    def getPrincipalCityInformation(self):
        
        city_id = self.data['id']
        city_name = self.data['name']
        country = self.data['sys']['country']
        
        return [city_id,city_name,country]
    
    def getPrincipalWeatherConditions(self):
        weather = self.data['weather']['main']
        
        #diccionary with temperatures
        temperatures = self.data['main']
        
        return [weather,temperatures]

        
    
    