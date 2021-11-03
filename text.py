# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt

@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series
  
  def get_name(col_name, serie):
   
    return col_name

  def get_unique(col_name, serie):
    
    return len(serie.unique())

  def get_missing(col_name, serie):
    return pd.isnull(serie).sum()

  def get_empty(col_name, serie):
    return (serie.values=='').sum()

  def get_whitespace(col_name, serie):
    
    return serie.str.contains(r'\s+').sum()

  def get_lowercase(col_name, serie):
    
    return serie.str.islower().sum()

  def get_uppercase(col_name, serie):
    
    return serie.str.isupper().sum()
  
  def get_alphabet(col_name, serie):
   
    return (serie.str.isalpha()).sum()

  def get_digit(col_name, serie):
   
    return (serie.str.isnumeric()).sum()

  def get_mode(col_name, serie):

    return serie.mode(dropna=True)[0]


  def get_barchart(col_name, serie):
    occur=serie.value_counts(ascending=False)
    occur1=occur.reset_index(inplace=False)
    #Displaying the occurance of only top 100 words as many words might lead to processinng issues and lack of clarity in the chart
    f=plt.figure(figsize=(10,5))
    ax=f.add_subplot(1,1,1)
    plt.bar(occur1.iloc[:100,0], occur1.iloc[:100,1])
    return f

  def get_frequent(col_name, serie):
    occur=serie.value_counts(ascending=False)
    occur1=occur.reset_index(inplace=False)
    total_num=occur1.iloc[:,1].sum()
    occur1['percentage']=occur1.iloc[:,1]*100/total_num
    return occur1