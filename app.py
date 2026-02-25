import streamlit as st 

st.title("OLA STREAMLIT APPLICATION")
st.header("OLA RIDE")

st.set_page_config(
    page_title="Ola Ride Analytics",
    page_icon="🚕",
    layout="wide"
)

st.markdown("<h1 style='text-align:center;'>🚖 Ola Ride Analytics Project</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📌 Project Overview")
    st.write("""
    This project analyzes **Ola ride booking data** to extract meaningful insights such as:
    - Successful and cancelled rides
    - Revenue trends
    - Customer and driver behavior
    - Vehicle performance
    """)

    st.subheader("📌 Problem Statement")
    st.write("""
    The rise of ride-sharing platforms has transformed urban mobility, offering convenience 
    and affordability to millions of users. OLA, a leading ride-hailing service, generates vast 
    amounts of data related to ride bookings, driver availability, fare calculations, and customer
     preferences. However, deriving actionable insights from this data remains a challenge. 
     
    To enhance operational efficiency, improve customer satisfaction, and optimize business 
    strategies, this project focuses on analyzing OLA’s ride-sharing data.By leveraging data 
    analytics, visualization techniques, and interactive applications,the goal is to extract
    meaningful insights that can drive data-informed decisions. 
             
    The project will involve cleaning and processing raw ride data, performing exploratory data 
    analysis (EDA), developing a dynamic Power BI dashboard, and creating a Streamlit-based web 
    application to present key findings in an interactive and user-friendly manner.
    """)

    st.subheader("🎯 Project Objectives")
    st.write("""
    - Execute SQL-based analysis  
    - Visualize ride data  
    - Integrate Power BI dashboards  
    - Build an interactive analytics app using Streamlit  
    """)

    st.subheader("🛠 Tech Stack")
    st.write("""
    - Python  
    - MySQL  
    - Pandas  
    - Streamlit  
    - Power BI  
    """)

with col2:
    st.image("assets/OLA_SYMBOL.jpg", use_container_width=True)
    st.image("assets/OLA_MOBILE.jpg",  use_container_width=True)
    
st.subheader("🎥 Project Dashboard")
st.image("assets/PAGE1.png")
st.image("assets/PAGE2.png")
st.image("assets/PAGE3.png")
st.image("assets/PAGE4.png")
st.image("assets/PAGE5.png")

st.markdown("---")
st.markdown("<p style='text-align:center;'>Created by <b>Jiya Shinde</b> 💚</p>", unsafe_allow_html=True)