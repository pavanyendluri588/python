#importing the pandas as pd
import pandas as pd
import openpyxl

#reading the csv file
file=pd.read_csv("csv_file.csv")

#converting to xls
"""
Excel File Extensions and Their Uses
XLS, XLSX, XLSM, XLTX and XLTM
"""
#for that we need openpyxl libary 
file.to_excel(r'csv_to_xls_converted.xlsx')
