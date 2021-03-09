# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:15:31 2021

@author: alejo
"""

import api
import data_weather_manager

ID = 1
CITY = 2 

def main():
    key = '0765a352299af83f9a0dcb84b1ac1c59'
    weather_api = api.WearherApi(key)
    data_manager = data_weather_manager.DataWeatherManager()
    
    option  = int(input('Insert an option: '))
    while option != 0:
        
    
        if option == CITY:
            name  = input('Please insert a city´s name: ')
           
            api_data = weather_api.getWeatherByName(name)
            data_manager.setData(api_data)
           
            city_info = data_manager.getPrincipalCityInformation()
            weather_data = data_manager.getPrincipalWeatherConditions()
            
            print('City name:' + city_info[1] + ', country: ' + city_info[2])
            print('Weather: ' + weather_data[0])
            
            print('TEMPERATURE: ' + str(weather_data[1]['temp']))
            print('Feels like: ' + str(weather_data[1]['feels_like']))
            
            option  = int(input('Insert an option: '))
        
        elif option == ID:
            city_id  = input('Please insert a city´s id: ')
            
            api_data = weather_api.getWeatherById(city_id)
            data_manager.setData(api_data)
            
            city_info = data_manager.getPrincipalCityInformation()
            weather_data = data_manager.getPrincipalWeatherConditions()
            
            
            print('City id:' + str(city_info[0]) + ', name: ' + city_info[1])
            
            print('TEMPERATURE: ' + str(weather_data[1]['temp']))
            print('Feels like: ' + str(weather_data[1]['feels_like']))
            
            option  = int(input('Insert an option: '))
        
        else:
            print('Bye')
        

main()
    
    