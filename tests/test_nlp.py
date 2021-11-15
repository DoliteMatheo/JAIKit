import unittest

from jaikit.nlp.word_segment import fmm_word_seg


class NLPTestCase(unittest.TestCase):
    def test_word_segment(self):
        self.assertEqual(["我们", "好多", "人", "啊"], fmm_word_seg(text="我们好多人啊"))
