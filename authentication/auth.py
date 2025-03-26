import streamlit as st

# User Credentials
USER_CREDENTIALS = {
    "admin": "pass123",
    "user1": "securepass"
}

# Initialize authentication state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["username"] = None

# Login Function
def login():
    st.title("Login")

    # Centered Layout
    col1, col2, col3 = st.columns([3, 2, 1])  # Center login form
    with col1:
        st.subheader("Enter Credentials")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

# Logout Function
def logout():
    st.session_state["authenticated"] = False
    st.session_state["username"] = None
    st.sidebar.success("Logged out successfully!")

