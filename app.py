import streamlit as st

from EmotionDetection.emotion_detection import emotion_detector


st.title("Emotion Detector")
text = st.text_area("Enter some text to analyze")

if st.button("Analyze"):
    if text.strip():
        result = emotion_detector(text.strip())
        st.subheader(f"Dominant emotion: {result['dominant_emotion'].title()}")

        scores = {
            emotion: score
            for emotion, score in result.items()
            if emotion != "dominant_emotion"
        }
        st.bar_chart(scores)
    else:
        st.warning("Please enter some text.")
