# Emotion Detector - Final Project

## Project Name: AI-Based Emotion Detection Web Application

This project is a final submission for the IBM Developer Skills Network course **"Developing AI Applications with Python and Flask"**.

## Description

A Flask-based web application that uses the **IBM Watson NLP Emotion Detection** API to analyze input text and identify the dominant emotion from: **anger, disgust, fear, joy, and sadness**.

## Features

- Emotion detection via Watson NLP EmotionPredict API
- Formatted output with scores for all 5 emotions and the dominant emotion
- Error handling for blank inputs (returns "Invalid text! Please try again")
- Unit tests with `unittest`
- Static code analysis with `pylint` (10.0/10.0 score)
- Flask web interface deployment

## Project Structure

```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
└── README.md
```

## How to Run

```bash
pip install flask requests pylint
python server.py
```

Visit `http://localhost:5000` in your browser.
