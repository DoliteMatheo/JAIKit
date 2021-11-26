import math
from decimal import Decimal
from typing import Union
from unittest import TestCase

from jaikit.datascience.calculate import (
    calc_cos_sim,
    calc_auc,
    calc_precision_recall_f1, calc_idf,
)


def compare_under_precision(
    a: Union[str, int, float], b: Union[str, int, float], precision: str = "0.000001"
) -> bool:
    """按约定的小数位数比较两个数值是否相等"""
    return Decimal(a).quantize(Decimal(precision)) == Decimal(b).quantize(
        Decimal(precision)
    )


class CalculateTestCase(TestCase):
    def test_calc_cos_sim(self):
        self.assertTrue(
            compare_under_precision(
                calc_cos_sim(vector_a=[0, 1], vector_b=[1, 1]), math.sqrt(2) / 2
            )
        )

    def test_calc_idf(self):
        docs = ["我们的未来", "我把他的作业看了一半", "我没有问题", "ABCD啊"]
        self.assertTrue(compare_under_precision(calc_idf(word="未来", all_docs=docs), 0.693147))
        self.assertTrue(compare_under_precision(calc_idf(word="的", all_docs=docs), 0.287682))
        self.assertTrue(compare_under_precision(calc_idf(word="我", all_docs=docs), 0.0))

    def test_calc_auc(self):
        y_true = [1] * 3 + [0] * 5
        y_pred = [0.8, 0.7, 0.3, 0.5, 0.6, 0.9, 0.4, 0.2]
        self.assertEqual(calc_auc(y_true, y_pred), 0.6)

    def test_calc_precision_recall_f1(self):
        y_true = [1, 1, 0, 1, 0]
        y_pred = [0, 1, 1, 1, 1]
        self.assertEqual(
            calc_precision_recall_f1(y_true, y_pred),
            (1 / 2, 2 / 3, 2 * 2 / (5 + 2 - 0)),
        )
