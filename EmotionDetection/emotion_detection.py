"""Emotion detection using a pretrained Hugging Face Transformer."""

from transformers import pipeline

# Load the pretrained emotion classification model
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None,
)


def _normalize_emotion_label(label):
    """Convert model labels to the canonical lowercase names used by the app."""
    if not isinstance(label, str):
        return str(label).lower()

    normalized = label.strip().lower().replace("-", "_")
    aliases = {
        "label_0": "sadness",
        "label_1": "joy",
        "label_2": "love",
        "label_3": "anger",
        "label_4": "fear",
        "label_5": "surprise",
        "label_6": "neutral",
    }
    return aliases.get(normalized, normalized)


def emotion_detector(text_to_analyze):
    """Detect emotions in the given text and return the predictions."""
    if text_to_analyze is None:
        raise ValueError("Text to analyze must be a non-empty string.")

    text = str(text_to_analyze).strip()
    if not text:
        return {
            "neutral": 1.0,
            "dominant_emotion": "neutral",
        }

    predictions = emotion_classifier(text)
    if predictions and isinstance(predictions[0], list):
        predictions = predictions[0]

    result = {}
    for prediction in predictions:
        if isinstance(prediction, dict):
            label = prediction.get("label", "unknown")
            score = prediction.get("score", 0.0)
            emotion = _normalize_emotion_label(label)
            result[emotion] = float(score)

    if not result:
        return {
            "neutral": 1.0,
            "dominant_emotion": "neutral",
        }

    dominant_emotion = max(result, key=result.get)
    result["dominant_emotion"] = dominant_emotion
    return result