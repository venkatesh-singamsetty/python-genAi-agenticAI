import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# 1. Setup Streamlit page config and title
st.set_page_config(page_title="SkyBook - Flight Booking", page_icon="✈️", layout="wide")

st.title("✈️ SkyBook: Hyderabad to Goa")
st.markdown("Book your flights easily from **Hyderabad (HYD)** to **Goa (GOI)** and back.")

# 2. Create dummy flight data using Pandas
def get_flight_data():
    # Outbound: HYD -> GOI
    outbound_data = {
        "Airline": ["IndiGo", "SpiceJet", "Air India", "Vistara", "Akasa Air"],
        "Flight No": ["6E-532", "SG-102", "AI-884", "UK-992", "QP-112"],
        "Departure": ["06:00 AM", "09:30 AM", "01:15 PM", "05:45 PM", "09:00 PM"],
        "Duration": ["1h 15m", "1h 20m", "1h 10m", "1h 25m", "1h 15m"],
        "Price": [3500, 3200, 4100, 5500, 3000]
    }
    
    # Inbound: GOI -> HYD
    inbound_data = {
        "Airline": ["IndiGo", "SpiceJet", "Air India", "Vistara", "Akasa Air"],
        "Flight No": ["6E-539", "SG-108", "AI-889", "UK-995", "QP-118"],
        "Departure": ["08:00 AM", "11:30 AM", "03:15 PM", "07:45 PM", "10:30 PM"],
        "Duration": ["1h 15m", "1h 20m", "1h 10m", "1h 25m", "1h 15m"],
        "Price": [3600, 3300, 4200, 5600, 3100]
    }
    
    return pd.DataFrame(outbound_data), pd.DataFrame(inbound_data)

df_outbound, df_inbound = get_flight_data()

# 3. Implement date selectors
st.sidebar.header("📅 Travel Dates")
dept_date = st.sidebar.date_input("Departure Date", datetime.today())
ret_date = st.sidebar.date_input("Return Date", datetime.today() + timedelta(days=2))

if ret_date < dept_date:
    st.sidebar.error("Return date cannot be before departure date.")

# 4. Display flight options & 5. Selection logic
st.subheader(f"🛫 Outbound: Hyderabad (HYD) → Goa (GOI) | {dept_date.strftime('%d %b %Y')}")

# Helper to display flight options as a radio button list with formatted strings
def format_option(row):
    return f"{row['Airline']} ({row['Flight No']}) - {row['Departure']} - ₹{row['Price']} - {row['Duration']}"

# We use indices to track selection
outbound_options = [format_option(row) for index, row in df_outbound.iterrows()]
selected_outbound_idx = st.radio("Select Outbound Flight", range(len(outbound_options)), format_func=lambda x: outbound_options[x])

st.markdown("---")

st.subheader(f"🛬 Inbound: Goa (GOI) → Hyderabad (HYD) | {ret_date.strftime('%d %b %Y')}")
inbound_options = [format_option(row) for index, row in df_inbound.iterrows()]
selected_inbound_idx = st.radio("Select Return Flight", range(len(inbound_options)), format_func=lambda x: inbound_options[x])

st.markdown("---")

# 6. Calculate Total Price
outbound_flight = df_outbound.iloc[selected_outbound_idx]
inbound_flight = df_inbound.iloc[selected_inbound_idx]
total_price = outbound_flight["Price"] + inbound_flight["Price"]

st.subheader(f"💰 Total Fare: ₹{total_price}")

# 7. Booking Summary
if st.button("Book Ticket 🎟️"):
    if ret_date < dept_date:
        st.error("Please correct the dates before booking.")
    else:
        st.success("🎉 Booking Confirmed! Have a safe trip.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("🛫 **Outbound Flight**")
            st.write(f"**Date:** {dept_date.strftime('%d %b %Y')}")
            st.write(f"**Airline:** {outbound_flight['Airline']}")
            st.write(f"**Flight:** {outbound_flight['Flight No']}")
            st.write(f"**Time:** {outbound_flight['Departure']}")
            st.write(f"**Price:** ₹{outbound_flight['Price']}")
            
        with col2:
            st.info("🛬 **Return Flight**")
            st.write(f"**Date:** {ret_date.strftime('%d %b %Y')}")
            st.write(f"**Airline:** {inbound_flight['Airline']}")
            st.write(f"**Flight:** {inbound_flight['Flight No']}")
            st.write(f"**Time:** {inbound_flight['Departure']}")
            st.write(f"**Price:** ₹{inbound_flight['Price']}")
            
        st.markdown("### Thank you for choosing SkyBook! ✈️")
