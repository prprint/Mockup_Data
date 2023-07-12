#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system(' pip install faker')


# In[1]:


import pandas as pd


# In[2]:


from pprint import pprint
# data = [10,20,30,40,50,60]

data = {'Name': ['Tom', 'nick', 'krish', 'jack'],

        'Age': [20, 21, 19, 18]}
# df = pd.DataFrame(data, columns=['Numbers'])
df = pd.DataFrame(data)

pprint(df)


# In[6]:


import faker as f

import pandas as pd

from datetime import datetime

from pprint import pprint


def generate_date(f, st, end, rows) -> list:

    result = list()

    for i in range(rows):

        result.append(f.date_between_dates(date_start=st, date_end=end))

    return result


def random_vlue_from_list(f, l, len_l, exp_row):#มีข้อมูลที่อยู่ใน list ก็จะให้มัน random

    result = list() 

    for i in range(exp_row):

        result.append(l[f.pyint(min_value=0, max_value=len_l-1)])

    return result


def create_random_list_from_df(f, df, col_nm, exp_row):

    list_df_result = df[pd.notnull(df[col_nm])][col_nm].drop_duplicates().values

    return random_vlue_from_list(f, list_df_result, len(list_df_result), exp_row)


f = f.Faker()

number_records = 12000

result = list()


vin = open("vin.txt", "r").read()

data_id = open("data_id.txt", "r").read()

df_map = pd.read_csv('mockup_map_data_unit.csv')


vin = vin.split("\n")

data_id = data_id.split("\n")


col_gts = generate_date(f, datetime(2023,5,1), datetime(2023,6,11), number_records)

col_vin = random_vlue_from_list(f, vin, len(vin), number_records)

col_egt = create_random_list_from_df(f, df_map, 'Engine Type', number_records)

col_mt = create_random_list_from_df(f, df_map, 'Model Type', number_records)

col_tt = create_random_list_from_df(f, df_map, 'Transmission Type', number_records)

col_lo = generate_date(f, datetime(2021,1,1), datetime(2023,6,10), number_records)

col_country = ['THAILAND' for x in range(number_records)]

col_mile = create_random_list_from_df(f, df_map, 'Mileage', number_records)

col_data_id = random_vlue_from_list(f, data_id, len(data_id), number_records)

col_data = create_random_list_from_df(f, df_map, 'Data', number_records)

col_unit = create_random_list_from_df(f, df_map, 'Unit', number_records)

col_acq_time = ['2023-06-11 22:34:53' for x in range(number_records)]

col_ecu = create_random_list_from_df(f, df_map, 'ECU', number_records)


df = pd.DataFrame({

    'GTS File Generation Time' : col_gts,

    'VIN' : col_vin,

    'Engine Type' : col_egt,

    'Model Type' : col_mt,

    'Transmission Type' : col_tt,

    'L/O Date' : col_lo,

    'Country' : col_country,

    'Mileage' : col_mile,

    'Data_ID' : col_data_id,

    'Data' : col_data,

    'Unit' : col_unit,

    'RanDevu Acquisition Time' : col_acq_time,

    'ECU' : col_ecu

})

# df['GTS File Generation Time'] = pd.to_datetime(df['GTS File Generation Time'], format='%Y-%m-%d')

# df['L/O Date'] = pd.to_datetime(df['L/O Date'], format='%Y-%m-%d')


# df['MIS'] = (df['GTS File Generation Time'] - df['L/O Date']).dt.days/30

# df = df[["GTS File Generation Time", "VIN", "Engine Type", "Model Type", "Transmission Type", "L/O Date", "Country",

#    "Mileage", "MIS", "Data_ID", "Data", "Unit", "RanDevu Acquisition Time", "ECU"]]

# pprint(df)


# In[7]:


df.head()


# In[ ]:




