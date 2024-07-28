import streamlit as st
from groq import Client

def sentiment_analysis(text):
    """Sentiment Analysis"""
    try:
        client = Client(api_key='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')
        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": ("""**Act as a sentiment analysis expert. Analyze the provided text and determine the sentiment of each paragraph or sentence.**

        **Respond with one of the following:**

        * **positive**
        * **negative**
        * **neutral**
        * **I can't understand the sentiment of that text.** (If uncertain)

        **Avoid any other outputs or explanations.**

        **Text:**

        {text}
        """)
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            model="Llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

        

st.title("Sentiment Analysis App")
text = st.text_area("Enter your text here:", height=150)  # Multi-line text input

if st.button("Analyze"):
    result = sentiment_analysis(text)
    if result:
        st.success(f"Sentiment analysis result: {result}")
    else:
        st.warning("No result obtained. Please try again.")


