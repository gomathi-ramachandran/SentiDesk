# SentiDesk

## Overview
SentiDesk is an AI-powered sentiment analysis system designed for helpdesk environments. It utilizes advanced Natural Language Processing (NLP) and Automatic Speech Recognition (ASR) to analyze customer interactions, classify sentiments, and provide actionable insights for improving customer support services.

## Features
- **Speech-to-Text Conversion**: Converts audio-based customer interactions into text.
- **Sentiment Classification**: Categorizes sentiment as Positive, Negative, or Neutral.
- **Confidence Scoring**: Provides reliability scores for sentiment predictions.
- **Real-time Insights**: Interactive dashboard for monitoring sentiment trends and patterns.
- **Data Storage & Logging**: Maintains historical sentiment analysis records for further insights.

## Tech Stack
- **Frontend**: Streamlit (Interactive Dashboard)
- **Backend**: Python (Flask/FastAPI)
- **Machine Learning**: Transformer-based NLP models (BERT, RoBERTa)
- **Speech Processing**: ASR models for audio transcription
- **Database**: PostgreSQL / MongoDB

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/gomathi-ramachandran/SentiDesk.git
   cd SentiDesk
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
- Upload customer audio recordings via the dashboard.
- View transcribed text and sentiment classification.
- Analyze sentiment trends using interactive visualizations.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact
For any queries, reach out to [Gomathi Ramachandran](https://github.com/gomathi-ramachandran).
