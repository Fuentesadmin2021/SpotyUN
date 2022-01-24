import sqlite3
from sqlite3 import Error

def sql_conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    
    except Error:
        print(Error)

#dejar aca funciones mientras tanto
def close(con):
    con.close() 

def close(self):
    self.conexionbd.close()