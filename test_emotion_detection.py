import unittest
from unittest.mock import patch, Mock
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    @patch('requests.post')
    def test_emotion_detector(self, mock_post):
        # Set up mock responses based on input text to simulate the Watson NLP API
        def side_effect(url, json, headers, timeout=None):
            text = json['raw_document']['text']
            mock_resp = Mock()
            mock_resp.status_code = 200

            if "glad" in text:
                emotions = {'anger': 0.05, 'disgust': 0.02, 'fear': 0.01, 'joy': 0.9, 'sadness': 0.02}
            elif "mad" in text:
                emotions = {'anger': 0.9, 'disgust': 0.02, 'fear': 0.01, 'joy': 0.05, 'sadness': 0.02}
            elif "disgusted" in text:
                emotions = {'anger': 0.02, 'disgust': 0.9, 'fear': 0.01, 'joy': 0.05, 'sadness': 0.02}
            elif "sad" in text:
                emotions = {'anger': 0.02, 'disgust': 0.02, 'fear': 0.01, 'joy': 0.05, 'sadness': 0.9}
            elif "afraid" in text:
                emotions = {'anger': 0.02, 'disgust': 0.02, 'fear': 0.9, 'joy': 0.05, 'sadness': 0.01}
            else:
                emotions = {'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.0, 'sadness': 0.0}

            mock_resp.text = '{"emotionPredictions": [{"emotion": ' + str(emotions).replace("'", '"') + '}]}'
            return mock_resp

        mock_post.side_effect = side_effect

        # Test case for joy
        result_1 = emotion_detector("I am glad this happened")
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case for anger
        result_2 = emotion_detector("I am really mad about this")
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case for disgust
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case for sadness
        result_4 = emotion_detector("I am so sad about this")
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        # Test case for fear
        result_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
