import streamlit as st # Streamlit library ko import karte hain

# --- Main App Content ---
st.title("Personalized Welcome App 👋") # App ka title

# User se naam poochein
user_name = st.text_input("Apna naam enter karein:", "Guest")

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
    st.write(f"Hello, **{user_name}**! Welcome to your first interactive Streamlit app.")
elif message_type == "Detailed Message":
    st.write(f"Namaste, **{user_name}**! Aapka is khaas Streamlit application mein swagat hai. Yeh app aapko data ke saath interact karna sikhayega.")
    st.info("Tip: Aap sidebar mein options change karke message dekh sakte hain!")

st.write("---") # Another horizontal line
st.success("App ready hai! Apni pasand ka naam aur message type chunein.")

# Optional: Add a small footer
st.markdown("Developed with ❤️ using Streamlit.")
