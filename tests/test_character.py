import unittest

from jaikit.character.eng_chn import (
    contains_chinese,
    remove_chinese,
    chinese_eng_boundary,
)
from jaikit.character.unicode import character_unicode_info


class UnicodeTestCase(unittest.TestCase):
    def test_character_unicode_info(self):
        rst = character_unicode_info(character="我")
        self.assertDictEqual(
            {
                "平面": "0 BMP",
                "区段范围": "U+4E00..U+9FFF",
                "区段名称": "中日韩统一表意文字",
                "英文名称": "CJK Unified Ideographs",
                "码位数": "20,992",
                "已定义字元数": "20,989",
                "文字": "汉字",
                "start": 19968,
                "end": 40959,
                "Unicode编码": 25105,
            },
            rst.to_dict(),
        )

    def test_contains_chinese(self):
        self.assertTrue(contains_chinese(text="aa有汉字，123."))
        self.assertFalse(contains_chinese(text="145 no chinese!"))

    def test_remove_chinese(self):
        for n in range(100):
            self.assertEqual("aa，123.", remove_chinese(text="aa有汉字，123."))
            self.assertEqual("145 no chinese!", remove_chinese(text="145 no chinese!"))

    def test_chinese_eng_boundary(self):
        text = "cat 猫咪"
        self.assertEqual("猫咪", text[chinese_eng_boundary(text) :])
        text = "abcd efgh"
        self.assertEqual(None, chinese_eng_boundary(text))
