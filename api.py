#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="API Visualization",
    page_icon="📜",
    layout="wide",
)

st.title("경기도 민원 데이터 시각화")

url_1 = "https://raw.githubusercontent.com/seonseono/minwon/main/api_data/%EA%B2%BD%EA%B8%B0%EB%8F%84_%EB%A7%9E%EC%B6%A4%ED%98%95%ED%86%B5%EA%B3%84.csv"
@st.cache
def load_data_1():
    df1 = pd.read_csv(url_1, encoding="cp949", index_col=0)
    return df1

df1 = load_data_1()

df1['민원 일자'] = df1['민원 일자'].apply(str)
df1['민원 일자'] = pd.to_datetime(df1['민원 일자'])
df1.head()


area1 = px.line(df1, x="민원 일자", y="민원 건수", title='맞춤형 통계 (키워드 : 경기도)'
                   , width=900, height=500, markers=True)
area1.show()


area1_2 = px.bar(df1, x="민원 일자", y="민원 건수", title='맞춤형 통계 (키워드 : 경기도)'
                   , width=900, height=500)
area1_2.show()



url_2 = "https://raw.githubusercontent.com/seonseono/minwon/main/api_data/%EA%B2%BD%EA%B8%B0%EB%8F%84_%ED%95%B5%EC%8B%AC%ED%82%A4%EC%9B%8C%EB%93%9C.csv"
@st.cache
def load_data_2():
    df2 = pd.read_csv(url_2, encoding="cp949", index_col=0)
    return df2

df2 = load_data_2()


px.bar(df2, x="키워드", y="비중", title='핵심 키워드 (범위 : 경기도)', width=900, height=500)

area2 = px.bar(df2, x="비중", y="키워드", title='핵심 키워드 (범위 : 경기도)', width=900, height=500)
area2.show()


df2_2 = df2.iloc[:10]
df2_2

area2_2 = px.bar(df2_2, x="키워드", y="비중", title='경기도 민원 핵심 키워드 순위', width=900, height=500)
area2_2.show()



url_3 = "https://raw.githubusercontent.com/seonseono/minwon/main/api_data/%ED%82%A4%EC%9B%8C%EB%93%9C%ED%8A%B8%EB%A0%8C%EB%93%9C_%EA%B2%BD%EA%B8%B0%EB%8F%84.csv"
@st.cache
def load_data_3():
    df3 = pd.read_csv(url_3, encoding="cp949", index_col=0)
    return df3

df3 = load_data_3()


df3['민원 일자'] = df3['민원 일자'].apply(str)
df3['민원 일자'] = pd.to_datetime(df3['민원 일자'])
df3.head()


area3 = px.bar(df3, x="민원 일자", y="민원 건수", title='키워드 트렌드 : 경기도', width=900, height=500)
area3.show()


area3_2 = px.bar(df3, x="민원 일자", y="증가율", title='키워드 트렌드 : 경기도', width=900, height=500)
area3_2.show()


url_4 = "https://raw.githubusercontent.com/seonseono/minwon/main/api_data/%ED%82%A4%EC%9B%8C%EB%93%9C%ED%8A%B8%EB%A0%8C%EB%93%9C_%EC%B2%B4%ED%97%98%EA%B4%80.csv"
@st.cache
def load_data_4():
    df4 = pd.read_csv(url_4, encoding="cp949", index_col=0)
    return df4

df4 = load_data_4()

df4['민원 일자'] = df4['민원 일자'].apply(str)
df4['민원 일자'] = pd.to_datetime(df4['민원 일자'])
df4.head()


area4 = px.bar(df4, x="민원 일자", y="민원 건수", title='키워드 트렌드 : 체험관', width=900, height=500)
area4.show()


area4_2 = px.bar(df4, x="민원 일자", y="증가율", title='키워드 트렌드 : 체험관', width=900, height=500)
area4_2.show()


# 마우스 오버했을 때 민원 건수도 나오면 좋겠다<br/>
# 트렌드니까 나올 필요 없나?

url_5 = "https://raw.githubusercontent.com/seonseono/minwon/main/api_data/%EC%97%B0%EA%B4%80%EC%96%B4%EB%B6%84%EC%84%9D_%EA%B2%BD%EA%B8%B0%EB%8F%84.csv"
@st.cache
def load_data_5():
    df5 = pd.read_csv(url_5, encoding="cp949", index_col=0)
    return df5

df5 = load_data_5()


df5['분석 스코어'] = round(df5['분석 스코어'], 2)
df5.head(2)


area5 = px.bar(df5, x="키워드", y="분석 스코어", title='연관어 분석 : 경기도', width=900, height=500)
area5.show()


df_5_2 = df5.iloc[:10]
df_5_2.head(2)

area5_2 = px.bar(df_5_2, x="키워드", y="분석 스코어", title='연관어 분석 : 경기도', width=900, height=500)
area5_2.show()


url_6 = "https://raw.githubusercontent.com/seonseono/minwon/main/api_data/%EC%97%B0%EA%B4%80%EC%96%B4%EB%B6%84%EC%84%9D_%EC%B2%B4%ED%97%98%EA%B4%80.csv"
@st.cache
def load_data_6():
    df6 = pd.read_csv(url_6, encoding="cp949", index_col=0)
    return df6

df6 = load_data_6()


df6['분석 스코어'] = round(df6['분석 스코어'], 2)
df6.head(2)


df6_2 = df6.iloc[:10]
df6_2.head(2)


area6 = px.bar(df6_2, x="키워드", y="분석 스코어", title='연관어 분석 : 경기도', width=900, height=500)
area6.show()


