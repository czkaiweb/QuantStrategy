#! /usr/bin/python 

import tushare as ts
import pandas  as pd
import os
import sys
import json

data_store_path = os.environ['STOCK']+'/data/'

########### Set up my token for TuShare API ###################
ts.set_token('')
ind_api = ts.pro_api()

def FetchIndividual(in_pro_api = None,  in_ts_code = None  ,in_start_date = None , in_end_date = None ):
    individual_file = in_ts_code+ "_" + in_start_date + "_" + in_end_date +".csv"
    df = in_pro_api.index_daily( ts_code = in_ts_code, start_date = in_start_date , end_date = in_end_date )
    df.to_csv( data_store_path+individual_file )

if __name__ == '__main__':
    FetchIndividual( in_pro_api = ind_api, in_ts_code = '399300.SZ', in_start_date = '20150612' , in_end_date = '20160601' )
    FetchIndividual( in_pro_api = ind_api, in_ts_code = '000001.SH', in_start_date = '20150612' , in_end_date = '20160601' )
    FetchIndividual( in_pro_api = ind_api, in_ts_code = '399300.SZ', in_start_date = '20150101' , in_end_date = '20190401' )
    FetchIndividual( in_pro_api = ind_api, in_ts_code = '000001.SH', in_start_date = '20150101' , in_end_date = '20190401' )
    FetchIndividual( in_pro_api = ind_api, in_ts_code = '399300.SZ', in_start_date = '20190101' , in_end_date = '20190401' )
    FetchIndividual( in_pro_api = ind_api, in_ts_code = '000001.SH', in_start_date = '20190101' , in_end_date = '20190401' )

