# Emotion Classifier (Lexicon-Based NLP Project)

This project is a lightweight, rule-based emotion classification system that identifies human emotions from text using a handcrafted lexicon. It maps keywords to Plutchik’s core emotion categories: joy, sadness, anger, fear, surprise, disgust, anticipation, and trust.

The system processes input text by tokenizing and matching words against a predefined emotion dictionary. It then counts emotion occurrences and predicts the dominant emotion in the sentence. If no keywords are found, it returns a default neutral prediction.

Unlike deep learning approaches, this project does not use neural networks or large language models. Instead, it focuses on fundamental Natural Language Processing concepts such as text preprocessing, pattern matching, and rule-based classification. This makes it highly suitable for beginners who want to understand how emotion detection works at a basic level before moving on to more complex machine learning models.

The project also includes a simple command-line chatbot interface where users can enter text and receive real-time emotion predictions. Additionally, it contains a built-in evaluation function that calculates accuracy using a small labeled test dataset, helping measure the performance of the lexicon-based approach.

Features

* Lexicon-based emotion detection system
* Supports 8 primary Plutchik emotions
* Simple and interactive CLI chatbot
* Built-in accuracy evaluation on test samples
* No external ML libraries required

Tech Stack

* Python
* Regular Expressions (re module)
* Basic NLP techniques
