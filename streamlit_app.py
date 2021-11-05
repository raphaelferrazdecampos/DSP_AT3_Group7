# To be filled by students

import streamlit as st
import pandas as pd
from streamlit.proto.DataFrame_pb2 import DataFrame
#import matplotlib.pyplot as plt
from data import Dataset
from text import TextColumn
#from datetime import DateColumn

st.title ('Data Explorer Tool')

#STREAMLIT - COMMAND FOR DROP AND DRAG CSV FILE
st.header("Upload CSV file for analysis")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    st.header("Overall Information")

#st.write('**Name of Table is : **'+Dataset.get_name(df))
st.write('**Number of rows is :**'+ str(Dataset.get_n_rows(df)))
st.write('**Number of Columns is :**'+str(Dataset.get_n_cols(df)))
st.write('**Number of Duplicated Columns is :**'+str(Dataset.get_n_duplicates(df)))
st.write('**Number of Rows with Missing Values**'+str(Dataset.get_n_missing(df)))
    
st.write('**List of columns :**')
st.markdown(Dataset.get_cols_list(df))
st.write('**Types of Columns**')
st.table(Dataset.get_cols_dtype(df))
    
st.write('Select the number of rows to be displayes')
n_rows=st.slider('n_rows',5, 50)
    
st.write('**Top Rows of Table**')
st.table(Dataset.get_head(df, n_rows))
    
st.write('**Bottom Rows of Table**')
st.table(Dataset.get_tail(df, n_rows))
    
st.write('**Random Sample Rows of Table**')
st.table(Dataset.get_sample(df, n_rows))
    
st.write('**List of columns :**')
st.markdown(Dataset.get_cols_list(df))
st.write('**Types of Columns**')
st.table(Dataset.get_cols_dtype(df))

st.write('Select the column to be converted to Date Time format')
option=st.selectbox('Columns', Dataset.get_cols_list(df))
df[option]=pd.to_datetime(df[option])
    
num=Dataset.get_numeric_columns(df)
text=Dataset.get_text_columns(df)
date=Dataset.get_date_columns(df)
    
#st.write(num)
#st.write(text)
#st.write(date)
    
for i in text:
    TextColumn.text_col_analysis(df[i], i)
for i in date:
    DateColumn.date_col_analysis(df[i],i)