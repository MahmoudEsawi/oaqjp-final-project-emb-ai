"""
Flask server for the Emotion Detection application.
Provides endpoints for rendering the main interface and analyzing text emotions.
"""

import os
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyzes the text passed via request parameters and returns
    a formatted string of emotion scores and the dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Process text through the emotion detector package
    result = emotion_detector(text_to_analyze)

    # Task 7: Handling of blank input errors
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the primary web interface template (index.html).
    """
    return render_template("index.html")

if __name__ == "__main__":
    # Get port from environment or default to 5000 (standard port)
    app_port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=app_port)
