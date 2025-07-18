import requests
import json

def emotion_detector(text_to_analyze):
    URL = ('https://sn-watson-emotion.labs.skills.network/'
    'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT_JSON = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=INPUT_JSON, headers=HEADERS, timeout=10)
    formatted_res = json.loads(response.text)

    emotions = formatted_res["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions, key=emotions.get)
    return emotions
