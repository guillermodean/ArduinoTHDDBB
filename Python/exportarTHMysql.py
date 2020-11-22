# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:51:28 2020

@author: Usuario
"""

import MySQLdb as MDB
import csv

QUERY="SELECT * FROM `thtable` ORDER BY `thtable`.`ID` DESC";

db=MDB.connect(
        host='localhost',
        user='root',
        db='thdata',
        password='Guillermo11'
            )
cur=db.cursor()
cur.execute(QUERY)
result= cur.fetchall()
print (result);

c=csv.writer(open('dbdump3.csv','w'))
for x in result:
    c.writerow(x);
