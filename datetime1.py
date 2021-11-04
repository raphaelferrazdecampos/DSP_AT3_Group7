from os import name
import streamlit as st
from dataclasses import dataclass
import pandas as pd
import matplotlib.pyplot as plt


@dataclass
class DateColumn:
    col_name: str
    serie: pd.Series

    
    def get_name(self):
        """
        Return name of selected column
        """
        name_col = self.serie.name
        return name_col

    def get_unique(self):
        """
        Return number of unique values for selected column
        """
        num_unique = self.serie.nunique()
        return num_unique

    def get_missing(self):
        """
        Return number of missing values for selected column
        """
        num_missing = self.serie.isnull().sum()
        return num_missing

    def get_weekend(self):
        """
        Return number of occurrence of days falling during weekend (Saturday and Sunday)
        """
        num_weekend = (self.serie.dt.day_name().isin(['Saturday', 'Sunday'])).sum()
        return num_weekend

    def get_weekday(self):
        """
        Return number of weekday days (not Saturday or Sunday)
        """
        num_weekday = (~self.serie.dt.day_name().isin(['Saturday', 'Sunday'])).sum()
        return num_weekday

    def get_future(self):
        """
        Return number of cases with future dates (after today)
        """
        today = pd.to_datetime("today")
        num_futureday = (self.serie > today).sum()
        return num_futureday

    def get_empty_1900(self):
        """
        Return number of occurrence of 1900-01-01 value
        """
        year_1900 = pd.to_datetime("1900-01-01")
        num_1900 = (self.serie.dt.date == year_1900).sum()
        return num_1900

    def get_empty_1970(self):
        """
        Return number of occurrence of 1970-01-01 value
        """
        year_1970 = pd.to_datetime("1970-01-01")
        num_1970 = (self.serie.dt.date == year_1970).sum()
        return num_1970

    def get_min(self):
        """
        Return the minimum date
        """
        date_min = min(self.serie)
        return str(date_min)

    def get_max(self):
        """
        Return the maximum date
        """
        date_max = max(self.serie)
        return str(date_max)

    def get_barchart(self):
        """
        Return the generated bar chart for selected column
        """
        count_bar = self.serie.value_counts()
        count_bar=count_bar.reset_index(inplace=False)
        f=plt.figure(figsize=(10,5))
        ax=f.add_subplot(1,1,1)
        plt.bar(count_bar.iloc[:,0], count_bar.iloc[:,1])
        return f

    def get_frequent(self):
        """
        Return the Pandas dataframe containing the occurrences and percentage of the top 20 most frequent values
        """
        df_frequency = self.serie.value_counts().to_frame()
        df_frequency = df_frequency.reset_index()
        df_frequency.columns = ['value', 'occurrence']
        df_frequency['percentage'] = df_frequency.occurrence.apply(lambda x: x / len(df_frequency))
        df_frequency = df_frequency.head(20)
        return df_frequency



'''
Inst_DataColumn = DateColumn()

data = {'value': [str(Inst_DataColumn.get_unique()), str(Inst_DataColumn.get_missing()), str(Inst_DataColumn.get_weekend()), str(Inst_DataColumn.get_weekday()),
                  str(Inst_DataColumn.get_future()),str(Inst_DataColumn.get_empty_1900()), str(Inst_DataColumn.get_empty_1970()),Inst_DataColumn.get_min(),Inst_DataColumn.get_max()]}
df_summary = pd.DataFrame(data, index=[
    "Number of Unique Values", "Number of Rows Missing Values",
    "Number of Weekend Dates", "Number of Weekday Dates",
    "Number of Dates in Future", "Number of Rows with 1900-01-01",
    "Number of Rows with 1970-01-01","Minimum Value","Maximum Value"])

sub_header = "Field Name:" + Inst_DataColumn.get_name()
st.subheader(sub_header)
st.dataframe(df_summary)
st.subheader("Bar Chart")
st.bar_chart(Inst_DataColumn.get_barchart())
st.subheader("Most Frequent Values")
st.table(Inst_DataColumn.get_frequent())
'''