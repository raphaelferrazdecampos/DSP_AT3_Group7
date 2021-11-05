# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt

@dataclass
class NumericColumn:
  col_name: str
  serie: pd.Series
  def get_name(self):
      return self.col_name
  def get_unique(self):
      return len(self.serie.unique())

  def get_missing(self):
      return pd.isnull(self.serie).sum()

  def get_zeros(self):
      return (self.serie== 0).sum()
    
    
  def get_negatives(self):
      return (self.serie < 0).sum()

  def get_mean(self):
      return self.serie.mean()
  
  def get_std(self):
      return self.serie.std()
  
  def get_min(self):
      return self.serie.min()

  def get_max(self):
        return self.serie.max()

  def get_median(self):
    #Return the median value for selected column

    return self.serie.median()

  def get_histogram(self):
    #Return the generated histogram for selected column
    #count_hist = self.serie.value_counts()
    f=plt.figure(figsize=(10,5))
    ax=f.add_subplot(1,1,1)
    plt.hist(self.serie)
    return f

  def get_frequent(self):
  #Return the Pandas dataframe containing the occurrences and percentage of thetop 20 most frequent values
    serie_frequency = self.serie.value_counts()
    serie_frequency = serie_frequency.reset_index()
    serie_frequency.columns = ['value', 'occurrence']
    serie_frequency['percentage'] = serie_frequency.occurrence.apply(lambda x: x / len(serie_frequency))
    serie_frequency = serie_frequency.head(20)
    return serie_frequency

