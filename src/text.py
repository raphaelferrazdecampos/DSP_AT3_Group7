# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt

@dataclass
class TextColumn:
  col_name: str
  serie: pd.Series
  
  def get_name(self):
   
    return self.col_name

  def get_unique(self):
    
    return len(self.serie.unique())

  def get_missing(self):
    return pd.isnull(self.serie).sum()

  def get_empty(self):
    return (self.serie.values=='').sum()

  def get_whitespace(self):
    
    return self.serie.str.contains(r'\s+').sum()

  def get_lowercase(self):
    
    return self.serie.str.islower().sum()

  def get_uppercase(self):
    
    return self.serie.str.isupper().sum()
  
  def get_alphabet(self):
   
    return (self.serie.str.isalpha()).sum()

  def get_digit(self):
   
    return (self.serie.str.isnumeric()).sum()

  def get_mode(self):

    return self.serie.mode(dropna=True)[0]


  def get_barchart(self):
    occur=self.serie.value_counts(ascending=False)
    occur1=occur.reset_index(inplace=False)
    #Displaying the occurance of only top 100 words as many words might lead to processinng issues and lack of clarity in the chart
    f=plt.figure(figsize=(10,5))
    ax=f.add_subplot(1,1,1)
    plt.bar(occur1.iloc[:100,0], occur1.iloc[:100,1])
    return f

  def get_frequent(self):
    occur=self.serie.value_counts(ascending=False)
    occur1=occur.reset_index(inplace=False)
    total_num=occur1.iloc[:,1].sum()
    occur1['percentage']=occur1.iloc[:,1]*100/total_num
    return occur1