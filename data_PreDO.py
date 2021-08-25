import streamlit as st
import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit.components.v1 as components

def main():
    st.title("Welcome to Pan's data analysis tool")
    select_list = ['Data Overview', 'Data Preprocess']
    select = st.sidebar.selectbox('Selec your action',select_list)

    data_file = st.file_uploader('Please upload your data file',type = ['xlsx','xls','csv'])
    if data_file is not None:
        file_type = get_type(data_file.name)
        read_status = True
        if file_type == 'xlsx' or file_type == 'xls' or file_type == 'XLSX' or file_type == 'XLS':
            try:
                read_data = pd.read_excel(data_file,encoding='gb18030')
            except UnicodeDecodeError:
                try:
                    read_data = pd.read_excel(data_file, encoding='utf-8')
                except UnicodeDecodeError:
                    st.warning('文件解码失败，请尝试使用记事本打开文件，再另存为，编码选择ASIN')
                    read_status = False
        else:
            try:
                read_data = pd.read_csv(data_file,encoding='gb18030')
            except UnicodeDecodeError:
                try:
                    read_data = pd.read_csv(data_file, encoding='utf-8')
                except UnicodeDecodeError:
                    st.warning('文件解码失败，请尝试使用记事本打开文件，再另存为，编码选择ASIN')
                    read_status = False
        if read_status:
            st.subheader("Data Summary")
            st.write(read_data)
    if select == 'Data Overview':
        if st.button('Generate Profile Report'):
            try:
                profile = ProfileReport(read_data)
                st_profile_report(profile)
            except UnboundLocalError:
                st.warning("Please upload your data firstly!")



def get_type(name_str):
    return name_str.split('.')[-1]

if __name__ == '__main__':
    main()