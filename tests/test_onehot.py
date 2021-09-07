import unittest

import pandas as pd

from jaikit.datascience.one_hot import series_onehot_converter

mock_df = pd.DataFrame([[2, 4.3], [5, 7.2], [8, 9]], columns=["c_int", "c_float"])


class OnehotConverterTestCase(unittest.TestCase):
    def test_one_hot_converter(self):
        self.assertTrue(
            series_onehot_converter(series=mock_df["c_int"], dimension=8)
            .astype("int64")  # 注意series_onehot_converter中get_dummies出来的dtypes是uint类型
            .equals(
                pd.DataFrame(
                    [
                        [0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1],
                    ]
                )
            )
        )
        self.assertRaises(ValueError, series_onehot_converter, mock_df["c_int"], 7)
        self.assertRaises(TypeError, series_onehot_converter, mock_df["c_float"], 9)
