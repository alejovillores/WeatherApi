# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:15:31 2021

@author: alejo
"""



def main():
    key = '0765a352299af83f9a0dcb84b1ac1c59'
    weather_api = api.WearherApi(key)
    
    data = weather_api.getWeatherById(3853354)
    data_manager = data_weather_manager.DataWeatherManager(data)
    
    values = data_manager.getPrincipalCityInformation()

    print("Id: " + str(values[0]))    
    print("Name: " + values[1])
    print("Country: " + values[2])
    

main()
    
    