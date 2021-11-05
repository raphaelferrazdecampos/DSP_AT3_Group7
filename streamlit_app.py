# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:38:17 2021

@author: Ayush
"""
#import sys
#sys.path.append('D:\MS Sem II\DSP\at3\src')
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data import Dataset
from text import TextColumn
from datetime1 import DateColumn
from numeric import NumericColumn

def num_col_analysis(serie, name):
    num_col=NumericColumn(name, serie)
    st.title('Field Name'+NumericColumn.get_name(num_col))
    st.write('**Number of Unique Values :**'+str(NumericColumn.get_unique(num_col)))
    st.write('**Number of rows with Missing Values :**'+str(NumericColumn.get_missing(num_col)))
    st.write('**Number of rows with Zeros :**'+str(NumericColumn.get_zeros(num_col)))
    st.write('**Number of rows with Negative Values :**'+str(NumericColumn.get_negatives(num_col)))
    st.write('**Average Value :**'+str(NumericColumn.get_mean(num_col)))
    st.write('**Standard Deviation Value :**'+str(NumericColumn.get_std(num_col)))
    st.write('**Minimum Value :**'+str(NumericColumn.get_min(num_col)))
    st.write('**Maximum Value :**'+str(NumericColumn.get_max(num_col)))
    st.write('**Median Value :**'+str(NumericColumn.get_median(num_col)))
    st.write('**Histogram**')
    st.pyplot(NumericColumn.get_histogram(num_col))
    st.write('**Most Frequent Values :**')
    st.write(NumericColumn.get_frequent(num_col))


def text_col_analysis(serie, name):
    text_col=TextColumn(name, serie)
    st.title('Field Name :'+TextColumn.get_name(text_col))
    st.write('**Number of Unique Values : **'+str(TextColumn.get_unique(text_col)))
    st.write('**Number of Rows with Missinng Values :**'+str(TextColumn.get_missing(text_col)))
    st.write('**Number of Empty rows :**'+str(TextColumn.get_empty(text_col)))
    st.write('**Number of Rows with only WhiteSpaces: **'+str(TextColumn.get_whitespace(text_col)))
    st.write('**Number of Rows with only Lower Cases: **'+str(TextColumn.get_lowercase(text_col)))
    st.write('**Number of Rows with only Upper Cases: **'+str(TextColumn.get_uppercase(text_col)))
    st.write('**Number of Rows with only Alphabets: **'+str(TextColumn.get_alphabet(text_col)))
    st.write('**Number of Rows with only Digits: **'+str(TextColumn.get_digit(text_col)))
    st.write('**Mode Value :**'+TextColumn.get_mode(text_col))
    st.write('**Bar Chart for Occurance of Values **')
    #st.bar_chart(TextColumn.get_barchart(text_col))
    st.pyplot(TextColumn.get_barchart(text_col))
    st.write('**Most Frequent Values **')
    st.write(TextColumn.get_frequent(text_col))

def date_col_analysis(serie,name):
    date_col=DateColumn(name, serie)
    st.title('Field Name :'+DateColumn.get_name(date_col))
    st.write('**Number of Unique Values : **'+str(DateColumn.get_unique(date_col)))
    st.write('**Number of Missing Values : **'+str(DateColumn.get_missing(date_col)))
    st.write('**Number of Days Falling during the Weekend (Saturday and Sunday) : **'+str(DateColumn.get_weekend(date_col)))
    st.write('**Number of Weekday Days : **'+str(DateColumn.get_weekday(date_col)))
    st.write('**Number of Cases with Future Dates : **'+str(DateColumn.get_future(date_col)))
    st.write('**Number of Occurence of 1900-01-01 : **'+str(DateColumn.get_empty_1900(date_col)))
    st.write('**Number of Occurence of 1970-01-01 : **'+str(DateColumn.get_empty_1970(date_col)))
    st.write('**Minimum Date : **'+str(DateColumn.get_min(date_col)))
    st.write('**Maximum Date : **'+str(DateColumn.get_max(date_col)))
    st.write('**Bar Chart**')
    #st.write(DateColumn.get_barchart(date_col))
    st.bar_chart(DateColumn.get_barchart(date_col))
    st.write('**Most Frequent Values**')
    st.write(DateColumn.get_frequent(date_col))


st.title ('Data Explorer Tool')

#STREAMLIT - COMMAND FOR DROP AND DRAG CSV FILE
st.header("Upload CSV file for analysis")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    st.header("Overall Information")

    dataob=Dataset(uploaded_file.name, df)

    st.write('**Name of Table is : **'+Dataset.get_name(dataob))
    st.write('**Number of rows is :**'+ str(Dataset.get_n_rows(dataob)))
    st.write('**Number of Columns is :**'+str(Dataset.get_n_cols(dataob)))
    st.write('**Number of Duplicated Columns is :**'+str(Dataset.get_n_duplicates(dataob)))
    st.write('**Number of Rows with Missing Values**'+str(Dataset.get_n_missing(dataob)))
    
    st.write('**List of columns :**')
    st.markdown(Dataset.get_cols_list(dataob))
    st.write('**Types of Columns**')
    st.table(Dataset.get_cols_dtype(dataob))
    
    st.write('Select the number of rows to be displayes')
    n_rows=st.slider('n_rows',5, 50)
    
    st.write('**Top Rows of Table**')
    st.table(Dataset.get_head(dataob, n_rows))
    
    st.write('**Bottom Rows of Table**')
    st.table(Dataset.get_tail(dataob, n_rows))
    
    st.write('**Random Sample Rows of Table**')
    st.table(Dataset.get_sample(dataob, n_rows))
    
    st.write('Select the column to be converted to Date Time format')
    option=st.selectbox('Columns',['None']+ Dataset.get_cols_list(dataob))
    
    if option != 'None':
        df[option]=pd.to_datetime(df[option])
    
    st.write('**List of columns :**')
    st.markdown(Dataset.get_cols_list(dataob))
    st.write('**Types of Columns**')
    st.table(Dataset.get_cols_dtype(dataob))
    
    num=Dataset.get_numeric_columns(dataob)
    text=Dataset.get_text_columns(dataob)
    date=Dataset.get_date_columns(dataob)
    
    #st.write(num)
    #st.write(text)
    #st.write(date)
    
    for i in num:
        num_col_analysis(df[i],i)
    for i in text:
        text_col_analysis(df[i], i)
    for i in date:
        date_col_analysis(df[i],i)
    