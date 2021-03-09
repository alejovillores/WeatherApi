# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 08:51:10 2021

@author: alejo
"""

class DataWeatherManager:
    
    def __init__(self,data = 0):
        self.data = data
    
    def getPrincipalCityInformation(self):
        final_data = []
        if self.data != 0:
            city_id = self.data['id']
            city_name = self.data['name']
            country = self.data['sys']['country']
        
            final_data = [city_id,city_name,country]
        
        return final_data
        
    def setData(self,data):
        self.data = data

    def getPrincipalWeatherConditions(self):
        final_data = []
        if self.data != 0:
            weather = self.data['weather'][0]['main']
        
            #diccionary with temperatures
            temperatures = self.data['main']
        
            final_data = [weather,temperatures]
        
        return final_data
    
    def getWeatherExtraData(self):
        final_data = []
        if self.data != 0:
            clouds = self.data['clouds']['all']
            visibility = self.data['visibility']
            wind_speed = self.data['wind']['speed']
            
            final_data = [clouds,visibility,wind_speed]
        
        return final_data
            
  
            

        
    
    