#! /usr/bin/python 

import tushare as ts
import pandas  as pd
import os
import sys
import json
from Tushare.python.SQLutilities import *

data_store_path = os.environ['STOCK']+'/data/'

########### Set up my token for TuShare API ###################
ts.set_token('')
ind_api = ts.pro_api()

def CheckStartDate(list_date, required_date):
    if list_date > required_date:
        return list_date
    else:
        return required_date

def FetchBasicInfo(in_pro_api , in_ts_code):
    basic_info = in_pro_api.stock_basic(ts_code = in_ts_code, list_status = 'L', fields = 'ts_code, exchange, name, list_date')
    print basic_info
    info_line  = str(basic_info).split('\n')[1]
    stock_code = info_line.split()[1].replace(".","_")
    stock_name = info_line.split()[2]
    list_date  = info_line.split()[4]
    return stock_code , stock_name, list_date


def FetchIndividual(in_pro_api = None,  in_ts_code = None , in_adj = None , in_asset = 'E' , in_start_date = None , in_end_date = None , in_freq = 'D' ,in_factors = []):
    stock_code, stock_name , list_date = FetchBasicInfo( in_pro_api , in_ts_code)
    list_date = CheckStartDate(list_date, in_start_date)
    individual_file = stock_code+".csv"
    df = ts.pro_bar( pro_api = in_pro_api , ts_code = in_ts_code, adj = in_adj, asset = in_asset, start_date = list_date , end_date = in_end_date, factors = in_factors )
    # Get basic info
    api_basic = ts.pro_api( )
    df_basic = api_basic.daily_basic( ts_code = in_ts_code , start_date = list_date , end_date = in_end_date , fields = 'ts_code,trade_date,turnover_rate,turnover_rate_f,volume_ratio,pe,pe_ttm,pb,ps,ps_ttm,total_share,float_share,free_share,total_mv,circ_mv' )
    # Combine DataFrame
    df_all = pd.merge(df,df_basic, how='left', on=['ts_code','trade_date'])
    InsertDataToSQL(df_all,"test")

if __name__ == '__main__':
#    FetchIndividual( in_pro_api = ind_api, in_ts_code = '000001.SZ', in_adj = None , in_asset = 'E',in_start_date = '19900101' , in_end_date = '20190301', in_factors = [])
#    FetchIndividual( in_pro_api = ind_api, in_ts_code = '600507.SH', in_adj = None , in_asset = 'E',in_start_date = '19900101' , in_end_date = '20190301', in_factors = [])
    FetchIndividual( in_pro_api = ind_api, in_ts_code = '601398.SH', in_adj = None , in_asset = 'E',in_start_date = '20190101' , in_end_date = '20190401', in_factors = [])

