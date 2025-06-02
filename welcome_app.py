import streamlit as st # Streamlit library ko import karte hain

# --- Main App Content ---
st.title("Welcome App 👋") # App ka title

# User se naam poochein
user_name = st.text_input("Apna naam enter karein:", "SIETn")

# --- Sidebar Content ---
st.sidebar.header("Message Options") # Sidebar ke liye heading

# Radio buttons for message type selection
message_type = st.sidebar.radio(
    "Kis tarah ka message chahiye?",
    ("Simple Message", "Detailed Message")
)

# --- Display Welcome Message based on selection ---
st.write("---") # Ek horizontal line for separation

if message_type == "Simple Message":
    st.write(f"Hello, **{user_name}**! main SHIVAM apka swagat krta hun.")
elif message_type == "Detailed Message":
    st.write(f"Namaste, **{user_name}**! Aapka is khaas Streamlit application me swagat hai. ye mera pahla web app hai jaha me welcome krna sikh rha")
    st.info("Tip: Aap sidebar mein options change karke message dekh sakte hain!")

st.write("---") # Another horizontal line
st.success("App ready hai! Apni pasand ka naam aur message type chunein.")

# Optional: Add a small footer
st.markdown("Developed by SHIVAM☠️.")
