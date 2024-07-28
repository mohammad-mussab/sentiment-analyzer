<p align="center">
  Sentiment Analyzer
</p>

Welcome to the Sentiment Analyzer app! This app is using  **Llama3-8b-8192** most advanced and foundational model for Open Sources models. It analyze the sentiment of the input text and categorize it as positive, negative, or neutral.


## Overview
The Sentiment Analyzer app is built using Streamlit, making it easy to deploy interactive web applications. It leverages Groq API for sentiment analysis, ensuring accurate and efficient results.

## Features
- Analyzes sentiment of the provided text
- Categorizes sentiment as positive, negative, or neutral
- User-friendly interface

## Installation
To get started with the Sentiment Analyzer app, follow these steps:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/sentiment-analyzer.git
   cd sentiment-analyzer
2. **Generate an API Key**
Obtain your API key from Groq. It's free and easy to get started.

3. **Add API Key**
- Go to the `.streamlit` folder.
- Open the `secrets.toml` file.
- Add your API key in the following format:
  ```toml
  [groq]
  GROQ_API = "YOUR_API_KEY"

4. **Install Required Packages**
  ```sh
  pip install -r requirements.txt
```
5. **Run the App**
```sh
streamlit run streamlit_app.py
```

## Preview
You can preview the Sentiment Analyzer app hosted on Streamlit Cloud by visiting the following link: [Sentiment Analyzer Preview](https://sentiment-analyzer-7.streamlit.app/)
Feel free to modify the app according to your needs.

## Contributing 
Contributions are welcome! If you have any ideas, suggestions, or improvements, please create a pull request or open an issue.
