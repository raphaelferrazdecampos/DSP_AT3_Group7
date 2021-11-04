# To be filled by students
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import  numpy as np

@dataclass
class NumericColumn:
  col_name: str
  serie: pd.Series
#--------------------------------------------------------------------------------
## source of data used for this section
## file_url=('https://www.kaggle.com/anthonypino/melbourne-housing-market')
##file_url = ('Melbourne_housing_FULL.csv')
#--------------------------------------------------------------------------------
  def get_name(self):
  #Return name of selected column

    return self.col_name

  def get_unique(self):
    #Return number of unique values for selected column

    return len(serie.unique())

    def get_missing(self):
    # Return number of missing values for selected column
    return pd.isnull(serie).sum()

  def get_zeros(self):
    #Return number of occurrence of 0 value for selected column
    return (self.serie== 0).sum(axis = 1)
    # where axis= 1 specifies sum operates on rows and o for columns
  def get_negatives(self):
    #Return number of negative values for selected column
      return (serie < 0).sum(axis = 1)

  def get_mean(self):
    #Return the average value for selected column
     return self.serie.mean()
   def get_std(self):
     #Return the standard deviation value for selected column

    return self.serie.std()
  
  def get_min(self)
    #Return the minimum value for selected column

    return self.serie.min()

  def get_max(self):
    #Return the maximum value for selected column

    return self.serie.max()

  def get_median(self):
    #Return the median value for selected column

    return self.serie.median()

  def get_histogram(self):
    #Return the generated histogram for selected column
    count_serie = self.series.count()
    coun_hist = hist(count_serie)
    return count_hist

  def get_frequent(self):
  #Return the Pandas dataframe containing the occurrences and percentage of thetop 20 most frequent values
    serie_frequency = self.serie.counts().frame()
    serie_frequency = serie_frequency.reset_index()
    serie_frequency.columns = ['value', 'occurrence']
    serie_frequency['percentage'] = serie_frequency.occurrence.apply(lambda x: x / len(serie_frequency))
    serie_frequency = serie_frequency.head(20)
    return serie_frequency

