import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


def run():
    #membuat judul
    st.title('Mushroom classification')
    #membuat sub header
    st.subheader('Milestone 2')
    #menambahkan deskripsi
    st.write('Page is made by Andryan wijaya')
    #tambahkan gambar
    image = Image.open('dataset-cover.jpg')
    st.image(image, caption = 'Mushroom')

    #show dataframe
    st.write('# Data')
    data = pd.read_csv('secondary_data.csv',delimiter=';')
    st.dataframe(data)

    st.write('# Barplot Cap diameter')
    fig = plt.figure(figsize=(15,5))
    data['cap-diameter'].plot.box()
    st.pyplot(fig)
    st.write()

    st.write('# Bar Cap shape')
    fig = plt.figure(figsize=(15,5))
    data['cap-shape'].value_counts().plot.bar()
    st.pyplot(fig)

    st.write('# Bar Cap surface')
    fig = plt.figure(figsize=(15,5))
    data['cap-surface'].value_counts().plot.bar()
    st.pyplot(fig)

    st.write('# Bar habitat')
    fig = plt.figure(figsize=(15,5))
    data['habitat'].value_counts().plot.bar()
    st.pyplot(fig)

    st.write('# Bar season')
    fig = plt.figure(figsize=(15,5))
    data['season'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    st.write('# Bar class')
    fig = plt.figure(figsize=(15,5))
    data['class'].value_counts().plot(kind='bar')
    st.pyplot(fig)

    st.write('# Bar Cap color')
    fig = plt.figure(figsize=(15,5))
    data['cap-color'].value_counts().plot.bar()
    st.pyplot(fig)

    st.write('# Bar stem height')
    fig = plt.figure(figsize=(15,5))
    data['stem-height'].plot.box()
    st.pyplot(fig)

    st.write('# Bar stem width')
    fig = plt.figure(figsize=(15,5))
    data['stem-width'].plot.box()
    st.pyplot(fig)
    
    st.write('# Bar setm root')
    fig = plt.figure(figsize=(15,5))
    data['stem-root'].value_counts().plot.bar()
    st.pyplot(fig)

    st.write('# Bar stem surface')
    fig = plt.figure(figsize=(15,5))
    data['stem-surface'].value_counts().plot.bar()
    st.pyplot(fig)


if __name__ == '__main__':
    run()