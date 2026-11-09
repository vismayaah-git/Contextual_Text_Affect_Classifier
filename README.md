# Contextual Text Affect Classifier

## Project Overview

Contextual Text Affect Classifier is a Python NLP application that uses deep learning with a pretrained Hugging Face Transformer model to identify emotions expressed in text. Its Streamlit interface lets users enter text and view the predicted dominant emotion alongside scores for each emotion.

## Model

The project uses the pretrained `j-hartmann/emotion-english-distilroberta-base` model from Hugging Face.

The model analyzes the given text and predicts the most likely emotion.

## Emotion Detection

The application can detect emotions such as:

- Joy
- Sadness
- Anger
- Fear
- Disgust
- Surprise
- Neutral

## Application

The Streamlit application allows users to:

- Enter a passage
- See the dominant emotion
- View the model's emotion scores


## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- Pytest

## Project Structure

```text
Contextual_Text_Affect_Classifier/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── requirements.txt
├── README.md
├── app.py
├── test_emotion_detection.py
└── .gitignore
```

## How to Run

1. Create a virtual environment

```powershell
python -m venv .venv
```

2. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

3. Install the required libraries

```powershell
pip install -r requirements.txt
```

4. Run the Streamlit application

```powershell
python -m streamlit run app.py
```

5. Streamlit opens the application in your browser. Enter text and choose **Analyze**.

## Testing

Run the automated tests using:

```powershell
pytest
```

## Project Outcome

Built a Python Streamlit application that uses deep learning with a pretrained Transformer model to classify text into seven emotion categories. The app displays the dominant emotion and a score chart for all categories, and the emotion detection function is covered by five automated tests.
```