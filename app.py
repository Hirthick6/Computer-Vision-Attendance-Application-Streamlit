import streamlit as st
import face_recognition

# Custom imports
from multipage import MultiPage
from pages import markAttendance, newEntry, viewAttendance, welcomePage  # import your pages here

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Attendance Application")

# Add all your applications (pages) here

app.add_page("Welcome", welcomePage.app)
app.add_page("Enter a new Student", newEntry.app)
app.add_page("Mark Your Attendance", markAttendance.app)
app.add_page("View Attendance Sheets", viewAttendance.app)

# The main app
app.run()
