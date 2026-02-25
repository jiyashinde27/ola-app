import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
from db_config import get_connection
import matplotlib.pyplot as plt
import altair as alt

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="qwertyuiopmnbvcxz!@12",
        database="ola"
    )

st.set_page_config(
    page_title="Ola Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Ola Ride Analytics Dashboard")
st.markdown("Select a question to view SQL results and insights 👇")
st.markdown("---")

conn = get_connection()

questions = [
    "1. Retrieve all successful bookings",
    "2. Average ride distance for each vehicle type",
    "3. Total number of cancelled rides by customers",
    "4. Top 5 customers with highest bookings",
    "5. Rides cancelled by drivers (personal & car issues)",
    "6. Max & Min driver ratings for Prime Sedan",
    "7. Rides paid using UPI",
    "8. Average customer rating per vehicle type",
    "9. Total booking value of successful rides",
    "10. Incomplete rides with reason"
]

choice = st.selectbox("📌 Choose a Question", questions)

# 1️⃣ Successful bookings
if choice.startswith("1"):
    st.subheader("✅ Successful Bookings")

    query = """
    SELECT *
    FROM cleaned_data
    WHERE Booking_Status = 'Success'
    """

    st.code(query, language="sql")
    df = pd.read_sql(query, conn)

    st.metric("Total Successful Rides", len(df))
    st.dataframe(df)

# 2️⃣ Average ride distance per vehicle
elif choice.startswith("2"):
    st.subheader("🚗 Average Ride Distance per Vehicle Type")

    query = """
    SELECT Vehicle_Type, AVG(Ride_Distance) AS Avg_Distance
    FROM cleaned_data
    GROUP BY Vehicle_Type
    """

    st.code(query, language="sql")
    df = pd.read_sql(query, conn)

    st.dataframe(df)
    fig = px.bar(df, x="Vehicle_Type", y="Avg_Distance", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

# 3️⃣ Cancelled rides by customers
elif choice.startswith("3"):
    st.subheader("❌ Cancelled Rides by Customers")

    query = """
    SELECT COUNT(*) AS total_customer_cancellations
    FROM cleaned_data
    WHERE Is_Canceled_by_Customer_TF = 'TRUE'
    """

    st.code(query, language="sql")
    df = pd.read_sql(query, conn)

    st.metric("Total Cancelled Rides", df.iloc[0, 0])

    fig, ax = plt.subplots()
    ax.bar(["Customer Cancelled Rides"], df.iloc[0, 0])
    ax.set_ylabel("Number of Rides")
    ax.set_title("Customer Cancelled Rides Count")

    st.pyplot(fig)

# 4️⃣ Top 5 customers
elif choice.startswith("4"):
    st.subheader("👥 Top 5 Customers by Number of Rides")

    query = """
    SELECT Customer_ID, COUNT(*) AS Total_Rides
    FROM cleaned_data
    GROUP BY Customer_ID
    ORDER BY Total_Rides DESC
    LIMIT 5
    """

    st.code(query, language="sql")
    df = pd.read_sql(query, conn)

    st.dataframe(df)
    fig = px.bar(df, x="Customer_ID", y="Total_Rides", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

# 5️⃣ Driver cancellations
elif choice.startswith("5"):
    st.subheader("🚫 Driver Cancellations (Personal & Car Issues)")

    query = """
    SELECT COUNT(*) AS driver_cancelled_rides
    FROM cleaned_data
    WHERE Is_Canceled_by_Driver_TF = 'TRUE'
    AND Canceled_Rides_by_Driver = 'Personal & Car related issue'
    """

    # Show SQL query on UI
    st.code(query, language="sql")
    
    # ✅ Execute query
    df = pd.read_sql(query, conn)

    # ✅ KPI
    total = int(df.iloc[0, 0])
    st.metric("Driver Cancelled Rides", total)

    # ✅ Bar chart (better than pie for single value)
    fig, ax = plt.subplots()
    ax.bar(["Personal & Car Issues"], [total])
    ax.set_ylabel("Number of Rides")
    ax.set_title("Driver Cancellations (Personal & Car Issues)")

    st.pyplot(fig)

# 6️⃣ Max & Min driver ratings (Prime Sedan)
elif choice.startswith("6"):
    st.subheader("⭐ Driver Ratings for Prime Sedan")

    query = """
    SELECT 
        MAX(Driver_Ratings) AS Max_Rating,
        MIN(Driver_Ratings) AS Min_Rating
    FROM cleaned_data
    WHERE Vehicle_Type = 'Prime Sedan'
    """

    st.code(query, language="sql")
    df = pd.read_sql(query, conn)

    col1, col2 = st.columns(2)
    col1.metric("Max Rating", df["Max_Rating"][0])
    col2.metric("Min Rating", df["Min_Rating"][0])

# 7️⃣ UPI payments
elif choice.startswith("7"):
    st.subheader("💳 Rides Paid Using UPI")

    query = """
    SELECT *
    FROM cleaned_data
    WHERE Payment_Method = 'UPI'
    """

    st.code(query, language="sql")
    df = pd.read_sql(query, conn)

    st.metric("Total UPI Rides", len(df))
    st.dataframe(df)

# 8️⃣ Avg customer rating per vehicle
elif choice.startswith("8"):
    st.subheader("⭐ Average Customer Rating per Vehicle Type")

    query = """
    SELECT Vehicle_Type, AVG(Customer_Rating) AS Avg_Rating
    FROM cleaned_data
    GROUP BY Vehicle_Type
    """

    st.code(query, language="sql")
    df = pd.read_sql(query, conn)

    st.dataframe(df)
    fig = px.bar(df, x="Vehicle_Type", y="Avg_Rating", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

# 9️⃣ Total booking value (successful)
elif choice.startswith("9"):
    st.subheader("💰 Total Booking Value (Successful Rides)")

    query = """
    SELECT SUM(Booking_Value) AS Total_Revenue
    FROM cleaned_data
    WHERE Booking_Status = 'Success'
    """

    st.code(query, language="sql")
    df = pd.read_sql(query, conn)

    st.metric("Total Revenue", f"₹ {df['Total_Revenue'][0]:,.2f}")

# 🔟 Incomplete rides with reason
elif choice.startswith("10"):
    st.subheader("⚠️ Incomplete Rides with Reason")

    query = """
    SELECT Booking_ID, Incomplete_Rides_Reason
    FROM cleaned_data
    WHERE Incomplete_Rides = 1
    """

    df = pd.read_sql(query, conn)

    # KPI
    st.metric("Total Incomplete Rides", df["total_rides"].sum())

    # Show table
    st.dataframe(df)

    # Bar chart using Altair (best for Streamlit)
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Incomplete_Rides_Reason:N", title="Reason"),
        y=alt.Y("total_rides:Q", title="Number of Rides"),
        tooltip=["Incomplete_Rides_Reason", "total_rides"]
    ).properties(
        width=600,
        height=400,
        title="Incomplete Rides by Reason"
    )

    st.altair_chart(chart, use_container_width=True)

    


