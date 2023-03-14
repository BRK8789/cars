import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
logo = Image.open('swrnlogo.png')

#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 
st.set_page_config(page_title="Weather Dataset  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
st.title("CAR DATA SET EDA")
# File upload
uploaded_file = st.file_uploader("Choose CARS DATA SET csv")
if uploaded_file is not None:
    car=pd.read_csv(uploaded_file)
    st.dataframe(car)
    # Define the list of names
    names = ["21A21A6113-G.Karthik Bhaskar", "21A21A6133-L.Harsha Vardhan", "21A21A6108-G.Swarupa","21A21A6120-K.Prasad","21A21A6110-D.Shyam","21A21A6128-K.Syamala Devi","21A21A6122-K.Uma Sai Surya","21A21A6108-B.Krishna Sai Ram"]

    # Add the names to the sidebar
    st.sidebar.title("Project Team Members:")

    for name in names:
        st.sidebar.write(name)
    st.sidebar.title("Under The Guidance of :")
    st.sidebar.write("Dr.Bomma.Ramakrishna")
    # Data Cleaning
    null_values = car.isnull().sum()
    if any(null_values):
        car.fillna(car.mean(), inplace=True)

    # Value Counts
    st.write("Different types of makes and their count:")
    st.write(car['Make'].value_counts())

    # Filtering
    st.write("Records where Origin is Asia or Europe:")
    st.write(car[car['Origin'].isin(['Asia', 'Europe'])])

    # Removing unwanted records
    car = car[~(car['Weight'] > 4000)]
    st.write("Number of records after removing rows with weight above 4000:", len(car))

    # Applying function on a column
    car['MPG_City'] = car['MPG_City'].apply(lambda x: x + 3)
    st.write("Records where Horsepower is greater than 200:")
    st.write(car[car['Horsepower'] > 200])

    # Value Counts using Bar Chart
    car_make_counts = car['Make'].value_counts()
    st.write("Count of Different Makes:")
    st.bar_chart(car_make_counts)

    # Filtering using Pie Chart
    asia_europe_cars = car[car['Origin'].isin(['Asia', 'Europe'])]
    asia_count = asia_europe_cars[asia_europe_cars['Origin'] == 'Asia'].shape[0]
    europe_count = asia_europe_cars[asia_europe_cars['Origin'] == 'Europe'].shape[0]
    origin_counts = [asia_count, europe_count]
    origin_labels = ['Asia', 'Europe']

    # Create pie chart figure
    fig, ax = plt.subplots()
    ax.pie(origin_counts, labels=origin_labels, autopct='%1.1f%%')
    ax.set_title("Distribution of Cars by Origin")

    # Pass figure to st.pyplot()
    st.pyplot(fig)


    # Applying function on a column using Histogram
    mpg_city_values = car['MPG_City'].apply(lambda x: x + 3)
    fig, ax = plt.subplots()
    ax.hist(mpg_city_values, bins=20)
    st.write("Distribution of MPG_City Values After Adding 3:")
    st.pyplot(fig)

