import streamlit as st
import pandas as pd
import plotly.express as px
import os
from authentication.auth import login, logout
from modules.audio_processing import transcribe_audio
from modules.sentiment_analysis import perform_sentiment_analysis
from modules.file_operations import save_to_csv, load_csv
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


# File Paths
TRANSCRIPTION_FILE = "data/transcription.csv"
RESULTS_FILE = "data/sentiment_results.csv"

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["username"] = None

# Display login page if not authenticated
if not st.session_state["authenticated"]:
    login()
    st.stop()

# Sidebar Navigation
st.sidebar.title(f"Welcome, {st.session_state['username']} ")
page = st.sidebar.radio("Navigation", ["Upload & Analyze", "Dashboard", "Logout"])

# Logout functionality
if page == "Logout":
    logout()
    st.rerun()

# Upload & Analyze Page
if page == "Upload & Analyze":
    st.title("Upload and Analyze Audio")
    uploaded_audio = st.file_uploader("Upload an audio file (wav/mp3)", type=["wav", "mp3"])
    
    if uploaded_audio:
        st.audio(uploaded_audio, format="audio/wav")
        transcription = transcribe_audio(uploaded_audio)
        
        if transcription:
            st.subheader("Transcription")
            st.write(transcription)
            
            sentiment, confidence = perform_sentiment_analysis(transcription)
            st.subheader("Sentiment Analysis")
            st.write(f"**Sentiment:** {sentiment}")
            st.write(f"**Confidence:** {confidence:.2f}")
            
            # Save results
            save_to_csv(TRANSCRIPTION_FILE, pd.DataFrame({"Transcription": [transcription]}))
            save_to_csv(RESULTS_FILE, pd.DataFrame({"Text": [transcription], "Sentiment": [sentiment], "Confidence": [confidence]}))
            
            st.success("Sentiment analysis saved and updated.")

# Dashboard Page
elif page == "Dashboard":
    st.title("Sentiment Analysis Dashboard")
    
    if os.path.exists(RESULTS_FILE):
        results_df = load_csv(RESULTS_FILE)
        
        # Standardizing Sentiment Labels (Ensure Consistency)
        results_df["Sentiment"] = results_df["Sentiment"].replace({
            "POSITIVE": "Positive",
            "NEGATIVE": "Negative",
            "NEUTRAL": "Neutral"
        })

        # Summary Metrics
        total_calls = len(results_df)
        positive_calls = (results_df["Sentiment"] == "Positive").sum()
        negative_calls = (results_df["Sentiment"] == "Negative").sum()
        neutral_calls = (results_df["Sentiment"] == "Neutral").sum()

        # Display Metrics
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Calls", total_calls)
        col2.metric("Positive Calls", positive_calls, "+", delta_color="normal")
        col3.metric("Neutral Calls", neutral_calls, "=", delta_color="off")
        col4.metric("Negative Calls", negative_calls, "-", delta_color="inverse")

        # Confidence Trend Line Chart
        st.subheader("Confidence Score Trend")
        fig_line = px.line(
            results_df, x=results_df.index, y="Confidence", 
            color="Sentiment",
            title="Confidence Score Over Time",
            markers=True,
            color_discrete_map={"Positive": "green", "Neutral": "blue", "Negative": "red"}
        )
        st.plotly_chart(fig_line)

        # Sentiment Pie Chart
        st.subheader("Sentiment Distribution")
        sentiment_counts = results_df["Sentiment"].value_counts().reset_index()
        sentiment_counts.columns = ["Sentiment", "Count"]
        fig_pie = px.pie(
            sentiment_counts, names="Sentiment", values="Count", 
            title="Sentiment Breakdown", 
            color="Sentiment",
            color_discrete_map={"Positive": "green", "Neutral": "blue", "Negative": "red"},
            hole=0.0
        )
        st.plotly_chart(fig_pie)

        # Sentiment Bar Chart
        fig_bar = px.bar(
            sentiment_counts, x="Sentiment", y="Count", 
            title="Sentiment Count", 
            color="Sentiment", 
            color_discrete_map={"Positive": "green", "Neutral": "blue", "Negative": "red"}
        )
        st.plotly_chart(fig_bar)

        # Display Recent Calls
        st.subheader("Recent Calls")
        recent_calls = results_df.tail(10).reset_index(drop=True)
        recent_calls.index = recent_calls.index + 1 


        st.dataframe(recent_calls, use_container_width=True)
        # st.dataframe(results_df.tail(10), use_container_width=True)
        
    else:
        st.info("No sentiment data available. Please upload an audio file.")
