import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from PIL import Image
 

gold = pd.read_csv("Gold_data.csv")
gold.set_index('date', inplace=True)

st.title ('Gold Prediction Web App')


label = 'Select the Option:- '
options = ['Home page','Data Visualization','Actual v/s Predicted graphs','Forecasted Graph', 'Datewise Prediction','Batchwise prediction']
chart = st.sidebar.radio(label, options)
batch = ['First 10 Days', 'First 20 Days', 'Whole 30 Days']
col1, col2, col3 = st.columns(3)

dates = ['2021-12-22', '2021-12-23', '2021-12-24', '2021-12-25', '2021-12-26', '2021-12-27', '2021-12-28',
         '2021-12-29', '2021-12-30', '2021-12-31', '2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04',
         '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10', '2022-01-11',
         '2022-01-12', '2022-01-13', '2022-01-14', '2022-01-15', '2022-01-16', '2022-01-17', '2022-01-18',
         '2022-01-19', '2022-01-20']
price = ['4334.62',     '4325.87',     '4305.59',    '4283.91',    '4268.97',     '4260.96',    '4257.00',
         '4252.19',     '4243.82',     '4251.12',    '4256.60',    '4214.41',     '4120.07',    '4120.98',
         '4204.58',     '4249.06',     '4227.67',    '4181.15',    '4154.26',     '4188.14',    '4228.32',
         '4232.48',     '4218.20',     '4193.34',    '4175.73',    '4185.60',     '4204.02',    '4214.62',
         '4212.77',     '4199.21']
d10 = ['2021-12-22:- 4334.62',
       '2021-12-23:- 4325.87']
if chart == 'Home page':
    st.subheader('Business Objective:- ')
    st.write('Data provided is related to gold prices. The objective is to understand the underlying structure in your dataset and come up with a suitable forecasting model which can effectively forecast gold prices for the next 30 days.')
    image6 = Image.open('img_7.png')
    st.image(image6)

    st.subheader('Group Number 5 :-  ')
    st.write("""P-169 Gold price prediction
    
    
          1.Mr.Madhuresh Kumar
    2.Ms.Varsha Reddy
    3.Mr.Hemant Shinde
    4.Mr.Karan Patil
    5.Ms.Madhuri Varpe
    6.Mr.Omprasad Kolhal
    7.Ms.Shraddha Hukkeri
        """)
    st.write("""Under The Guidance:-
    
         1.Karthik
    2.Dhanyapriya     
        """ )
elif chart == 'Data Visualization':
 st.subheader('Line chart :- ')
 st.line_chart(gold)

 st.subheader('Bar chart :- ')
 st.bar_chart(gold)

 st.subheader('Histogram chart :- ')
 fig, ax = plt.subplots()
 ax.hist(gold)
 st.pyplot(fig)
elif chart == 'Actual v/s Predicted graphs':
 st.subheader('Train vs Predicted :- ')
 image = Image.open('img.png')
 st.image(image)

 st.subheader('Test vs Predicted :- ')
 image1 = Image.open('img_1.png')
 st.image(image1)
elif chart == 'Forecasted Graph':
    st.subheader('Next 30 Days Predicted Price Graph:- ')
    image2 = Image.open('img_2.png')
    st.image(image2)
elif chart == 'Batchwise prediction':
    with col1:
        d2 = st.selectbox('Select date batch', (batch))
    if d2 == 'First 10 Days':
        df1 = pd.read_csv("iris1.csv")
        df1
    elif d2 == 'First 20 Days':
        df2 = pd.read_csv("iris2.csv")
        df2
    elif d2 == 'Whole 30 Days':
       df3 = pd.read_csv("iris.csv")
       df3
    else:
        st.text('please')
elif chart == 'Datewise Prediction':
    col1, col2, col3 = st.columns(3)
    with col1:
        d1 = st.selectbox('Select Date', sorted(dates))
    if d1 == '2021-12-22':
        st.subheader('Gold Price:-  4234.62')
    elif d1 == '2021-12-23':
        st.subheader('Gold Price:-  4325.87')
    elif d1 == '2021-12-24':
        st.subheader('Gold Price:-  4305.59')
    elif d1 == '2021-12-25':
        st.subheader('Gold Price:-  4283.91')
    elif d1 == '2021-12-26':
        st.subheader('Gold Price:-  4268.97')
    elif d1 == '2021-12-27':
        st.subheader('Gold Price:-  4260.96')
    elif d1 == '2021-12-28':
        st.subheader('Gold Price:-  4257.00')
    elif d1 == '2021-12-29':
        st.subheader('Gold Price:-  4252.19')
    elif d1 == '2021-12-30':
        st.subheader('Gold Price:-  4243.82')
    elif d1 == '2021-12-31':
        st.subheader('Gold Price:-  4251.12')
    elif d1 == '2022-01-01':
        st.subheader('Gold Price:-  4256.60')
    elif d1 == '2022-01-02':
        st.subheader('Gold Price:-  4214.41')
    elif d1 == '2022-01-03':
        st.subheader('Gold Price:-  4120.07')
    elif d1 == '2022-01-04':
        st.subheader('Gold Price:-  4120.98')
    elif d1 == '2022-01-05':
        st.subheader('Gold Price:-  4204.58')
    elif d1 == '2022-01-06':
        st.subheader('Gold Price:-  4249.06')
    elif d1 == '2022-01-07':
        st.subheader('Gold Price:-  4227.67')
    elif d1 == '2022-01-08':
        st.subheader('Gold Price:-  4181.15')
    elif d1 == '2022-01-09':
        st.subheader('Gold Price:-  4154.26')
    elif d1 == '2022-01-10':
        st.subheader('Gold Price:-  4188.14')
    elif d1 == '2022-01-11':
        st.subheader('Gold Price:-  4228.32')
    elif d1 == '2022-01-12':
        st.subheader('Gold Price:-  4232.48')
    elif d1 == '2022-01-13':
        st.subheader('Gold Price:-  4218.20')
    elif d1 == '2022-01-14':
        st.subheader('Gold Price:-  4193.34')
    elif d1 == '2022-01-15':
        st.subheader('Gold Price:-  4175.73')
    elif d1 == '2022-01-16':
        st.subheader('Gold Price:-  4185.60')
    elif d1 == '2022-01-17':
        st.subheader('Gold Price:-  4204.02')
    elif d1 == '2022-01-18':
        st.subheader('Gold Price:-  4214.62')
    elif d1 == '2022-01-19':
        st.subheader('Gold Price:-  4212.77')
    elif d1 == '2022-01-20':
        st.subheader('Gold Price:-  4199.21')
    else:
        st.subheader('please select valid date')
else:
    st.subheader('select right option')















