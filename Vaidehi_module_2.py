# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:32:09 2022

@author: vaidehi Patole
"""

import pandas as pd
import os

os.getcwd()
os.chdir("C:\\Users\\vaide\OneDrive\\Desktop\\Week 2")

def json_file():
    json_ds = pd.read_json("nested_data.json")
    print(json_ds.head(15))
    return

def csv():
    csv_ds = pd.read_csv ("Neural_data.csv")
    print(csv_ds.head(15))
    return 
 
    
def excel_file():
   excel_ds = pd.read_excel("Excel_report.xlsx",sheet_name='financials',usecols=[12,26,27,28,29,33,34,35,37,38,39,40,41,42,43,44]) 
   print(excel_ds.head(15))
   return


def text_file():
    text_ds = pd.read_table("network_data.txt")    
    print(text_ds.head(15))
    return


if __name__ == "__main__":
    # Main functions to Run
    json_file()
    csv() 
    excel_file()
    text_file()
    
