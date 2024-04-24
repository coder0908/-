import streamlit as st
import pandas as pd

dataframe = pd.DataFrame({
    'first column': ['이름', '나이', '성별', '거주'],
    'second column': ['권다경', '17', '여성', '김포']
})

# 다운로드 버튼 연결
st.download_button(
    label='CSV로 다운로드',
    data=dataframe.to_csv(), 
    file_name='권다경.csv', 
    mime='text/csv'
)


