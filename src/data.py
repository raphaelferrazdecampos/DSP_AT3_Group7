# To be filled by students

from dataclasses import dataclass
import pandas as pd

@dataclass
class Dataset:
  name: str
  df: pd.DataFrame
  
  def get_name(self):
    
    return self.name

  def get_n_rows(self):
  
    return len(self.df)

  def get_n_cols(self):
    
    return len(self.df.columns)

  def get_cols_list(self):
    
    return list(self.df.columns.values)

  def get_cols_dtype(self):
    typ = {}
    for t in self.df.dtypes.to_dict():
      typ[t] = str(self.df.dtypes[t])
    
    types_data=pd.DataFrame.from_dict(typ,orient='index')

    return types_data

  def get_n_duplicates(self):
    duplicates_count=len(self.df)-len(self.df.drop_duplicates())
    return duplicates_count

  def get_n_missing(self):
    empty_count=len(self.df)-len(self.df.dropna())
    return empty_count

  def get_head(self, n=5):
    top=self.df.head(n+1)
    return top

  def get_tail(self, n=5):
    tail=self.df.tail(n)
    return tail

  def get_sample(self, n=5):
    random=self.df.sample(n)
    return random

  def get_numeric_columns(self):
    numeric_df=self.df.select_dtypes(include='number')
    numeric_list=list(numeric_df.columns)
    return numeric_list

  def get_text_columns(self):
    text_df=self.df.select_dtypes(include='object')
    text_list=list(text_df.columns)
    return text_list

  def get_date_columns(self):
    date_df=self.df.select_dtypes(include='datetime')
    date_list=list(date_df.columns)
    return date_list

  





