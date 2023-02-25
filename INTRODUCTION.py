import streamlit as st
import datetime
import time as t
from PIL import Image

araiwa = Image.open('hanger (3).png')
st.set_page_config(
    page_title='CLOSET',
    page_icon=(araiwa),
    layout='centered')


Menu_bar = st.progress(0)

st.title("WELCOME TO SEE SIZE YOUR STYLE!")

image = Image.open('IMG_1461.PNG')
st.image(image)


for Menu_bar_percent in range(100):
    t.sleep(0.00000000001)
    Menu_bar.progress(Menu_bar_percent + 1)


st.text_area( 'INTRODUCTION','''    Are you facing the problem of not knowing what to wear or not knowing your size?
    If you want to dress up in your style and can tell your clothing size We recommend our website.That can let you enjoy dressing and can make you size your clothes.
     ''')

col5,col6 = st.columns(2)
with col5:
    title = st.text_input('Name')
with col6:
    d = st.date_input(
         "DOB",
    datetime.date(2023, 2, 25))

col1, col2, col3, col4 = st.columns(4)
with col1:
    image = Image.open('IMG_1456.PNG')
    st.image(image)
with col2:
    image = Image.open('IMG_1457.PNG')
    st.image(image)
with col3:
    image = Image.open('IMG_1458.PNG')
    st.image(image)
with col4:
    image = Image.open('IMG_1459.PNG')
    st.image(image)





