from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        statements = ["I am glad this happened", "I am really mad about this",
                      "I feel disgusted just hearing about this", "I am so sad about this",
                      "I am really afraid that this will happen"
                      ]
        dom_ems = ["joy", "anger", "disgust", "sadness", "fear"]

        for i in range(len(statements)):
            res1 = emotion_detector(statements[i])
            self.assertEqual(res1["dominant_emotion"], dom_ems[i])

unittest.main()
