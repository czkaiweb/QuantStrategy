#! /usr/bin/python

import psycopg2
import pandas as pd
from Tushare.python.SQLMap import *
import pdb

##################### Establish the connection to SQL database
connect = psycopg2.connect(database="",user="",password="",host="127.0.0.1",port="5432")

print "Database on-line..."

def FormulateList(inlist,header):
    fstr = "("
    for i, item in enumerate(inlist):
        if header[i] == 'ts_code' and item != 'ts_code':
            fstr += "'"+str(item)+"'"+","
        else:
            fstr += str(item) + ","
    fstr = fstr.rstrip(',') + ")"
    return fstr

def CreateForm( header, form, cursor):
    create_cmd = "create table if not exists " + form
    create_cmd += "("
    for i,title in enumerate(header):
       # create_cmd += title + "  " + SQLType[title] + ( " primary key  not null, " if i == 0 else ",")
       create_cmd += title + "  " + SQLType[title] + ","
    create_cmd = create_cmd.rstrip(',')+ ");"
    cursor.execute(create_cmd)
    connect.commit()
#    pdb.set_trace()

def InsertDataToSQL(dataframe, form):
    cursor = connect.cursor()
    header = list(dataframe.columns.values)
    CreateForm(header, form, cursor)
    #### Loop over DataFrame and insert the data
    for index,row in dataframe.iterrows():
        insert_cmd ="insert into "+form
        insert_cmd += FormulateList(header,header)
        insert_cmd += " values "
        insert_cmd += FormulateList(map(lambda x: row[x],header),header ) 
        insert_cmd += ";"
        #print insert_cmd
        cursor.execute(insert_cmd)
    connect.commit()
    connect.close()
        
    
    


