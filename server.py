from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def RunSentimentAnalysis():
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    
    if response["dominant_emotion"] == None:
        return "Invalid text! Please try again!"
    
    keys = list(response.keys())
    vals = list(response.values())
    return (f"For the given statement, the system response is '{keys[0]}': {vals[0]}, "
             f"'{keys[1]}': {vals[1]}, '{keys[2]}': {vals[2]}, '{keys[3]}': {vals[3]}, "
             f"'{keys[4]}': {vals[4]}. The domination emotion is <b>{vals[5]}</b>."
            )

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
