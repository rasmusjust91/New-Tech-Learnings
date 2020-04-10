import unittest
from sort_algorithm import sort_algorithm


class TestSortingAlgorithm(unittest.TestCase):

    def test_sorting(self):
        self.assertEqual(
            sort_algorithm(
                [-6, -6, 5, 0, -234, 3, 5, 4, 2]
                ), [-234, -6, -6, 0, 2, 3, 4, 5, 5]
            )

    def test_list_input(self):
        self.assertRaises(TypeError, sort_algorithm, ['a', 5, 7])


if __name__ == '__main__':
    unittest.main()
