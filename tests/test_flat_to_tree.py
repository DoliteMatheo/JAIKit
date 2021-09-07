import unittest

from jaikit.datastructure.flat_to_tree import FlatRelationToTree

flat_info = [
    {"_id": 3, "name": "IT与通讯", "parent_id": None},
    {"_id": 4, "name": "互联网", "parent_id": 3},
    {"_id": 6, "name": "电子技术/半导体", "parent_id": 3},
    {"_id": 7, "name": "计算机硬件", "parent_id": 6},
    {"_id": 8, "name": "医疗器械", "parent_id": 9},
    {"_id": 9, "name": "制药/医疗", "parent_id": None},
    {"_id": 10, "name": "汽车", "parent_id": None},
    {"_id": 11, "name": "房地产", "parent_id": None},
]

tree_rst = {
    3: "IT与通讯",
    4: "IT与通讯-互联网",
    6: "IT与通讯-电子技术/半导体",
    7: "IT与通讯-电子技术/半导体-计算机硬件",
    8: "制药/医疗-医疗器械",
    9: "制药/医疗",
    10: "汽车",
    11: "房地产",
}


class FlatToTreeTestCase(unittest.TestCase):
    def test_id_to_whole_chain(self):
        mock_flat_to_tree = FlatRelationToTree(relations=flat_info)
        self.assertDictEqual(tree_rst, mock_flat_to_tree.id_to_whole_chain())
