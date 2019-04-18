#! /usr/bin/python

import psycopg2
import pandas as pd
from Tushare.python.SQLMap import *

##################### Establish the connection to SQL database
connect = psycopg2.connect(database="",user="",password="",host="127.0.0.1",port="5432")

print "Database on-line..."

cursor = connect.cursor()

def CreateForm( header, form):
    create_cmd = '''
            if( to_regclass('daily') is null ) then
            create table ''' + form
    create_cmd += "("
    for i,title in enumerate(header):
        create_cms += title + "  " + SQLtype[title] + " primary key  not null, " if i == 0 else ","
    create_cms += ";"

def InsertData(dataframe, form):
    header = list(dataframe.columns.values)
    cursor.execute( CreateForm(header, form) )
    


