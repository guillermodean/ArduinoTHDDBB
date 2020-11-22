# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:26:32 2020

@author: Usuario
"""

import datetime
import MySQLdb


#a = datetime.datetime.strptime('date', "%b %d %Y %H:%M");
#print ('a');
a= time.strftime("%d/%m/%y");
b=time.strftime("%H:%M:%S");
date= a+ ' '+b;
print(date);


#print(datetime.strftime("%H:%M:%S %d/%m/%y"));
"""
cursor.execute('INSERT INTO myTable (Date) VALUES(%s)', (a.strftime('%Y-%m-%d %H:%M:%S'),))
"""
#dt_object1 = datetime.datetime.strptime("%d/%m/%Y %H:%M:%S")
#print("dt_object1 =", dt_object1)