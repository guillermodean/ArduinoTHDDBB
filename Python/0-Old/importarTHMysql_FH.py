# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:15:52 2020

@author: Usuario
"""

#!/usr/bin/env python
 
import serial
import json
import MySQLdb
 
arduino = serial.Serial('COM4',9600) 
print (arduino.readline())
print (arduino.readline())
while True:
    character= arduino.readline()   
    MyJson = character
    db = MySQLdb.connect("localhost","root","Guillermo11","thdata")  
    if character != '\n':
        try:
            data=json.loads(character)
            print (data)
            print (data['Humedad'])
            curs = db.cursor()
            curs.execute("INSERT INTO `thtable2` (Fecha,Humedad,Temperatura) VALUES (now(),"+str(data['Humedad'])+","+str(data['Temperatura'])+")") 
        
        except ValueError as error:
            print ("no se ha podido enviar".format(error))
 
 
arduino.close()