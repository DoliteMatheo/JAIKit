import math
from typing import Union
from unittest import TestCase

from jaikit.datascience.calculate import (
    calc_cos_sim,
    calc_auc,
    calc_precision_recall_f1,
    calc_idf,
    calc_norm_vectors,
    check_array_equal,
)


def compare_under_precision(
    a: Union[str, int, float], b: Union[str, int, float], precision: float = 1e-5
) -> bool:
    """按约定的小数位数比较两个数值是否相等"""
    return math.isclose(float(a), float(b), rel_tol=precision)


class CalculateTestCase(TestCase):
    def test_calc_cos_sim(self):
        self.assertTrue(
            compare_under_precision(
                calc_cos_sim(vector_a=[0, 1], vector_b=[1, 1]), math.sqrt(2) / 2
            )
        )

    def test_calc_idf(self):
        docs = ["我们的未来", "我把他的作业看了一半", "我没有问题", "ABCD啊"]
        self.assertTrue(
            compare_under_precision(calc_idf(word="未来", all_docs=docs), 0.693147)
        )
        self.assertTrue(
            compare_under_precision(calc_idf(word="的", all_docs=docs), 0.287682)
        )
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

    def test_calc_norm_vectors(self):
        mock_vectors = [[3, 4], [7, 24], [0, 1]]
        right_answer = [[0.6, 0.8], [0.28, 0.96], [0.0, 1.0]]
        normed_vectors = calc_norm_vectors(vectors=mock_vectors)
        self.assertTrue(check_array_equal(normed_vectors, right_answer))

    def test_check_array_equal(self):
        arr1 = [0.6, 0.8]
        arr2 = [0.6000001, 0.8]
        arr3 = [[0.6, 0.8]]
        arr4 = [[0.61, 0.8], [1, 2]]
        arr5 = [[0.6100002, 0.8], [1, 2]]
        self.assertTrue(check_array_equal(arr1, arr2))
        self.assertFalse(check_array_equal(arr1, arr3))
        self.assertFalse(check_array_equal(arr3, arr4))
        self.assertTrue(check_array_equal(arr4, arr5))
