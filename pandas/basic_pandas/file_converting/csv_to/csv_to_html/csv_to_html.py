#importing pandas libary as pd
import pandas as pd
#reading the csv file
file=pd.read_csv("csv_file.csv")

#converting to html file
file.to_html("csv_file_to_html.html")
