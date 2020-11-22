# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:14:48 2020

@author: Usuario
"""

import MySQLdb
try:

    db = MySQLdb.connect(
            host="localhost",
            user="root",
            password="Guillermo11",
            db="thdata"
            )
except ValueError:
    print("no se ha podido conectqar");
    
cur=db.cursor();
try:
    cur.execute("INSERT INTO `users`(`ID`,`username`, `Password`, `fullname`) VALUES (9,'Marina','Raton','MGAyesa')");
    db.commit;
    print("Record inserted successfully into sql");
    cur.close();
except ValueError as error:
    print("Failed to insert record into Laptop table {}".format(error));
    
    
    """try:
    cur.execute('INSERT INTO `thtable` (Fecha,Humedad,Temperatura) VALUES (now(),34.0,1.0)');
    db.commit;
    print("Record inserted successfully into sql")
    cur.close();
except ValueError as error:
    print("Failed to insert record into Laptop table {}".format(error))
    
""" 