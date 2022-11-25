import unittest

from Lab5 import KMP_search

class MyTestCase(unittest.TestCase):

    def test_kmp(self) -> None:
        with open("Lab 5/test/test1.txt") as file:
            text1: str = file.readline()
        with open("Lab 5/test/test2.txt") as file:
            text2: str = file.readline()
        with open("Lab 5/test/test3.txt") as file:
            text3: str = file.readline()

        self.assertEqual(KMP_search("ABCDE", text1), [919])
        self.assertEqual(KMP_search("ABA", text2), [805, 852, 904, 930])
        self.assertEqual(KMP_search("AAAAAA", text3), [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308, 315, 322, 329, 336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504, 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637, 644, 651, 658, 665, 672, 679, 686, 693, 700, 707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798, 805, 812, 819, 826, 833, 840, 847, 854, 861, 868, 875, 882, 889, 896, 903, 916])
        self.assertEqual(KMP_search("FG", text3), -1)



        


if __name__ == '__main__':
    unittest.main()