# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 12:34:51 2021

@author: alejo
"""

from datetime import date
import matplotlib.pyplot as plt

class DataAnalitics:
    
    ''' Que va a poder hacer ?
    1) Leer data
    2) Guardar data
    3) Graficar data.'''
    
    def __init__(self,city_name):
        self.path = "C:/Users/alejo/Documents/Proyectos/WeatherApi/logs/"
        self.city_name = city_name
        self.currTime = date.today()
    
    def writeFile(self,city_data):
        file = open(self.path + self.city_name + '.csv','w')
        
        temperature = city_data['temperature']
        humidity = city_data['humidity']
        pressure = city_data['pressure']
        
        file.write(str(self.currTime) + ',' + str(temperature) + ',' + str(humidity) + ',' + str(pressure))
        file.close()
    
    def convertFileToList(self,file):
        data = []
        line = file.readline()
        while line:
            particular_date = line.strip().split(',')
            data.append(particular_date)
            line = file.readline()

        return data
    
    def readFile(self):
        try:
            file = open(self.path + self.city_name + '.csv','r')
            list_of_data = self.convertFileToList(file)
            file.close()
            return list_of_data
        except:
            print("Coudn´t open file.")
            return []
    
    def printData(self):
        list_of_values = self.readFile()
        if len(list_of_values) > 0:
            x = [] 
            y = []
            for item in list_of_values:
                x.append(item[0])
                y.append(item[1])
        
            plt.plot(x,y)
            plt.show()
        