import streamlit as st
import pandas as pd

st.title ('Overall Information of the dataset')

st.header("Upload CSV file for analysis")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

rows_count=len(df)
columns_count=len(df.columns)
duplicates_count=len(df)-len(df.drop_duplicates())
empty_count=len(df)-len(df.dropna())

st.header("Overall Information")
st.write("Filename: ", uploaded_file.name)
st.write("Number of Rows", rows_count)
st.write("Number of Columns", columns_count)
st.write("Number of Duplicated Rows", duplicates_count)
st.write("Number of Rows with missing values", empty_count)


typ = {}
for t in df.dtypes.to_dict():
    typ[t] = str(df.dtypes[t])

types_data=pd.DataFrame.from_dict(typ,orient='index')

st.header("Type of Columns")
st.write(types_data)

filter_rows=st.slider('top_rows',5,50,5)
top=df.head(filter_rows+1)
st.header("Top Rows")
st.write(top)

tail=df.tail(filter_rows)
st.header("Bottom Rows")
st.write(tail)

random=df.sample(filter_rows)
st.header("Random Rows")
st.write(random)

column_list=list(df.columns)
options=st.multiselect("Columns to be transformed in DateTime", column_list)

df[options]=df[options].apply(pd.to_datetime)

st.write(df)

