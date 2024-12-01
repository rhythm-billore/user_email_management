import streamlit as st
import sqlite3
import pandas as pd

# Create or connect to the database
conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS email_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT UNIQUE NOT NULL
)
""")
conn.commit()

# Streamlit App UI
st.title("Email Collection Portal")
st.subheader("Submit your email and view the list of stored emails")

# Form for Email Input
email = st.text_input("Enter your email address:")

if st.button("Submit"):
    if email:
        try:
            # Insert the email into the database
            cursor.execute("INSERT INTO email_table (email) VALUES (?)", (email,))
            conn.commit()
            st.success(f"Email '{email}' has been added successfully!")
        except sqlite3.IntegrityError:
            st.error(f"Email '{email}' is already in the database.")
    else:
        st.error("Please enter a valid email.")

# Display Stored Emails
st.subheader("Stored Emails:")
emails_df = pd.read_sql_query("SELECT * FROM email_table", conn)
st.dataframe(emails_df)

# Close the database connection when the app stops
conn.close()
