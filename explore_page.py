import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import pickle
import numpy as np

# Define constants
MAX_EXPERIENCE = 50

# Load model and encoders
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

# Define prediction function
def predict_salary(country, education, experience):
    X = np.array([[country, education, experience]])
    X[:, 0] = le_country.transform(X[:, 0])
    if education not in le_education.classes_:
        # Handle unseen education level (e.g., assign a default category)
        education = "Other"  # Or a more appropriate category

    X[:, 1] = le_education.transform(X[:, 1])
    X = X.astype(float)
    salary = regressor.predict(X)
    return salary

# Define UI creation function
def create_ui():
    st.title("Software Developer Salary Prediction")
    st.write("Please provide the following details to estimate the salary of a software developer.")

    country = st.selectbox("Country", ["United States", "India", "United Kingdom", "Germany", "Canada", "Brazil", "France", "Spain", "Netherlands", "Poland", "Italy", "Russian Federation", "Sweden"])
    education = st.selectbox("Education Level", ["Less than a Bachelors", "Bachelor's degree", "Master's degree", "Post grad"])
    experience = st.slider("Years of Experience", 0, MAX_EXPERIENCE, 3)

    ok = st.button("Compute Salary", key="Compute Salary")
    if ok:
        salary = predict_salary(country, education, experience)
        st.subheader(f"The estimated salary is ${salary[0]:,.2f}")

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Other"
    return categorical_map

def clean_experience(x):
    if x == "More than 50 years":
        return 50
    if x == "Less than 1 year":
        return 0.5
    return float(x)

def clean_education(x):
    if "Bachelor's degree" in x:
        return "Bachelor's degree"
    if "Master's degree" in x:
        return "Master's degree"
    if "Post grad" in x:
        return "Post grad"
    return "Less than a Bachelor's"

st.cache_data
def load_data():
    df = pd.read_csv("survey_result.csv")

    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()

    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)

    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    return df

df = load_data()

le_education = LabelEncoder()
le_education.fit(["Less than a Bachelors", "Bachelor's degree", "Master's degree", "Post grad"])  # Add "Bachelor's degree"

le_education = LabelEncoder()
le_education.fit(df["EdLevel"].unique())  # Fit with combined dataset

def show_explore_page():
    st.title("Explore Software Developer's Data")

    st.write(
        """ ### Stack Overflow Developer Survey """
    )

    data = df["Country"].value_counts().reset_index()
    data.columns = ['Country', 'Count']

    # Pie chart with Plotly
    fig1 = px.pie(data, names='Country', values='Count', title='Number of Data from Different Countries',
                  color_discrete_sequence=px.colors.sequential.RdBu, hole=0.3)

    fig1.update_traces(textinfo='percent+label')
    fig1.update_layout(template='plotly_dark')

    st.plotly_chart(fig1)

    # Experience vs Salary interactive scatter plot with animation
    df_sorted = df.sort_values(by='YearsCodePro')
    fig2 = px.scatter(df_sorted, x='YearsCodePro', y='Salary', color='Country',
                      title='Years of Experience vs. Salary',
                      labels={'YearsCodePro': 'Years of Experience', 'Salary': 'Salary'},
                      animation_frame='YearsCodePro', hover_data=['EdLevel'])

    fig2.update_layout(template='plotly_dark')

    st.plotly_chart(fig2)

    # Salary distribution by Education Level
    fig3 = px.box(df, x='EdLevel', y='Salary', color='EdLevel', title='Salary Distribution by Education Level',
                  labels={'EdLevel': 'Education Level', 'Salary': 'Salary'})

    fig3.update_layout(template='plotly_dark')

    st.plotly_chart(fig3)
