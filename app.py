import streamlit as st
import pandas as pd
from datetime import datetime

# Excel file path
FILE_PATH = "team_huddle.xlsx"

# Initialize excel if not exists
try:
    df = pd.read_excel(FILE_PATH)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Team ART", "Name", "Status", "Attendance"])
    df.to_excel(FILE_PATH, index=False)

st.set_page_config(page_title="Team HUDDLE", layout="centered")

st.title("📋 Team HUDDLE")

# Input fields
team_art = st.text_input("Team ART")
name = st.text_input("Name")
status = st.text_area("Status Update")
attendance = st.radio("Attendance", ["✅ Present", "❌ Absent"])

# Submit button
if st.button("Submit Update"):
    today = datetime.now().strftime("%Y-%m-%d")
    new_row = {"Date": today, "Team ART": team_art, "Name": name, "Status": status, "Attendance": attendance}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_excel(FILE_PATH, index=False)
    st.success("✅ Update saved!")

# Show table of today's updates
st.subheader("Today's Updates")
today = datetime.now().strftime("%Y-%m-%d")
st.dataframe(df[df["Date"] == today])
