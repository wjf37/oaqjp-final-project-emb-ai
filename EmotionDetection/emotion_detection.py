import requests
import json

def emotion_detector(text_to_analyze):
    URL = ('https://sn-watson-emotion.labs.skills.network/'
    'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    INPUT_JSON = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, json=INPUT_JSON, headers=HEADERS, timeout=10)
    emotions = {"anger": None, "disgust": None, "fear": None, 
                "joy": None, "sadness": None, "dominant_emotion": None
                }
    if response.status_code == 400:
        return emotions

    formatted_res = json.loads(response.text)

    emotions = formatted_res["emotionPredictions"][0]["emotion"]
    emotions["dominant_emotion"] = max(emotions, key=emotions.get)
    return emotions
