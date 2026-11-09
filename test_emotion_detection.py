from EmotionDetection.emotion_detection import emotion_detector


def test_happy_text():
    result = emotion_detector("I am extremely happy today!")
    assert result["dominant_emotion"] == "joy"


def test_sad_text():
    result = emotion_detector("I am feeling very sad and lonely.")
    assert result["dominant_emotion"] == "sadness"


def test_angry_text():
    result = emotion_detector("I am extremely angry about this.")
    assert result["dominant_emotion"] == "anger"


def test_fearful_text():
    result = emotion_detector("I am terrified of what might happen.")
    assert result["dominant_emotion"] == "fear"


def test_disgust_text():
    result = emotion_detector("That food was disgusting.")
    assert result["dominant_emotion"] == "disgust"