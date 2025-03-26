# SentiDesk: AI-Powered Sentiment Analysis for Helpdesk Calls

SentiDesk is an AI-driven sentiment analysis system designed to enhance helpdesk operations by analyzing customer calls. It uses speech recognition and transformer-based NLP models to classify sentiments as positive, negative, or neutral, providing real-time insights to improve customer service quality.

## Features
- **Automatic Speech Recognition (ASR)** for transcribing customer calls.
- **Sentiment Classification** using transformer-based NLP models (e.g., BERT, RoBERTa).
- **Real-time Visualization** with an interactive Streamlit dashboard.
- **Trend Analysis** for tracking sentiment patterns over time.
- **Confidence Score Metrics** to assess prediction reliability.

## Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/gomathi-ramachandran/SentiDesk.git
cd SentiDesk
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment
- **Windows (PowerShell):**
  ```sh
  venv\Scripts\Activate
  ```
- **Windows (CMD):**
  ```sh
  venv\Scripts\activate.bat
  ```
- **macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 5️⃣ Run the Application
```sh
streamlit run app.py
```

## Usage
1. Upload customer audio recordings via the dashboard.
2. View the transcribed text and sentiment classification.
3. Analyze sentiment trends and confidence scores with interactive visualizationson the dashboard.


## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve SentiDesk.

## Contact
For any queries, reach out to [Gomathi Ramachandran](https://github.com/gomathi-ramachandran).
