#/usr/bin/python 

import tushare as ts
import os
import sys
import time
from  Tushare.python.tushare_fetch_individual import *

##############  Setting up token  ##################
ts.set_token('')
fetch_list = ts.pro_api()

##############  List of stocks in SH   ##############
sh_list = fetch_list.hs_const(hs_type='SH')
sh_list = sh_list.head(10)
for index, line in sh_list.iterrows() :
    ind_api = ts.pro_api()
    if line['ts_code'].endswith(".SH"):
        FetchIndividual(in_pro_api = ind_api, in_ts_code = line['ts_code'], in_adj = None , in_asset = 'E',in_start_date = '19900101' , in_end_date = '20190301')


#############  List of stocks in SZ    ##############
sz_list = fetch_list.hs_const(hs_type='SZ')
sz_list = sz_list.head(10)
for index, line in sz_list.iterrows() :
    ind_api = ts.pro_api()
    if line['ts_code'].endswith(".SZ"):
        FetchIndividual(in_pro_api = ind_api, in_ts_code = line['ts_code'], in_adj = None , in_asset = 'E',in_start_date = '19900101' , in_end_date = '20190301')




