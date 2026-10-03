"""
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emo_detect():
    """
    This endpoint return emotional analysis given text
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emo_dict = emotion_detector(text_to_analyze)

    return f"""For the given statement,
    the system response is 'anger': {emo_dict['anger']},
    'disgust': {emo_dict['disgust']},
    'fear': {emo_dict['fear']},
    'joy': {emo_dict['joy']} and
    'sadness': {emo_dict['sadness']}.
    The dominant emotion is {emo_dict['dominant_emotion']}."""

@app.route("/")
def index():
    """"
    This function returns the home page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    