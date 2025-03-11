import streamlit as st
import re

# Function to Check Password Strength
def check_password_strength(password):
    strength = 0
    remarks = "Weak"
    
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    
    if strength == 5:
        remarks = "Very Strong"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 3:
        remarks = "Moderate"
    elif strength == 2:
        remarks = "Weak"
    else:
        remarks = "Very Weak"
    
    return strength, remarks

# Streamlit UI Styling
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #FFD700;
            font-family: 'Courier New', monospace;
            text-shadow: 4px 4px 10px #FFD700;
        }
        .password-box {
            background-color: #ADD8E6;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0px 0px 15px #FFD700;
            text-align: center;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 20px;
            color: #FFD700;
            font-family: 'Courier New', monospace;
            text-shadow: 2px 2px 5px #FFD700;
        }
        /* Custom Password Input Styling */
        input[type="password"] {
            background: transparent !important;
            border: 2px solid #FFD700 !important;
            box-shadow: 0px 0px 10px #FFD700 !important;
            color: #FFD700 !important;
            font-size: 18px !important;
            padding: 10px !important;
            border-radius: 8px !important;
        }
        input[type="password"]::placeholder {
            color: rgba(255, 215, 0, 0.5) !important;
        }
    </style>
""", unsafe_allow_html=True)

# UI Layout
st.markdown("<div class='main-title'>🔒 Password Strength Meter</div>", unsafe_allow_html=True)

password = st.text_input("Enter your password:", type="password", key="password")

if password:
    strength, remarks = check_password_strength(password)
    st.markdown(f"""
        <div class='password-box'>
            <h3>Strength Level: {strength}/5</h3>
            <h4>Remarks: {remarks}</h4>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='footer'>Made by Moin Sheikh</div>", unsafe_allow_html=True)
