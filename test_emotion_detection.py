import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ('I am really mad about this', 'anger'),
            ('I feel disgusted just hearing about this', 'disgust'),
            ('I am so sad about this', 'sadness'),
            ('I am really afraid this will happen', 'fear')
        ]

        for test_input, expected in test_cases:
            with self.subTest(test_input=test_input, expected=expected):
                self.assertEqual(emotion_detector(test_input)['dominant_emotion'], expected)

unittest.main()