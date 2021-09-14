import unittest

from jaikit.datastructure.max_match import MaxMatchTranslate


class MaxMatchTestCase(unittest.TestCase):
    def test_max_match(self):
        translate = MaxMatchTranslate(
            translate_map={
                "汽车": "automobile",
                "飞机": "plane",
                "机场": "airport",
                "飞机场": "airfield",
                "乘坐汽车": "take a car",
            }
        )
        self.assertEqual(
            "我们take a car到airfield了", translate.max_match_translate(text="我们乘坐汽车到飞机场了")
        )
