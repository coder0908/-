import streamlit as st
import pandas as pd

dataframe = pd.DataFrame({
    '1': ['name', 'age' , 'live'],
    '2': ['G.D.G', '17', 'gimpo']
})

# 다운로드 버튼 연결
st.download_button(
    label='CSV로 다운로드',
    data=dataframe.to_csv(), 
    file_name='권다경.csv', 
    mime='text/csv'
)


