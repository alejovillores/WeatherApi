# -*- coding: utf-8 -*-
"""
@author: alejo
"""

import requests
import json

class WearherApi :
    
    def __init__(self,key):
        self.url  = "https://api.openweathermap.org/data/2.5/weather?"
        self.key = key
    
    
    def getWeatherById(self, city_id):
        final_url = self.url + "id={}".format(str(city_id)) + "&appid=" + self.key
        r = requests.get(final_url)
        
        if  r.status_code == requests.codes.ok:
            return self.jsonLoader(r)
        else:
            return -1
    
    def getWeatherByName(self, city_name):
        final_url = self.url + "q={}".format(city_name) + "&appid=" + self.key
        r = requests.get(final_url)
        
        if  r.status_code == requests.codes.ok:
            return self.jsonLoader(r)
        else:
            return -1
    
    def jsonLoader(self,r):
        data = json.loads(r.content)
        return data
        
    
'''url ='https://api.openweathermap.org/data/2.5/weather?q=junin,ar&appid=0765a352299af83f9a0dcb84b1ac1c59' 
req = requests.get(url)
algo = json.loads(req.content)'''
