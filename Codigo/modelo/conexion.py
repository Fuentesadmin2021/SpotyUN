import sqlite3
from sqlite3 import Error

def sql_conexion():
    try:
        con = sqlite3.connect('SpotyUN.db')
        return con
    
    except Error:
        print(Error)

