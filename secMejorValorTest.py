import unittest

from secMejorValor import secMejorValor


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.files = secMejorValor()
        self.files.makeFilesValues("FUN.BB11001.tsv", "\t")
        self.files.makeFilesSeq("VAR.BB11001.tsv", "\n")

    #check errors in inputs
    def test_should_WrongInputFile_in_Fun_raise_an_exception(self):
        with self.assertRaises(Exception):
            self.files.makeFilesValues("nombreErroneo", "\t")

    def test_should_WrongInputFile_in_Val_raise_an_exception(self):
        with self.assertRaises(Exception):
            self.files.makeFilesSeq("nombreErroneo2", "\n")

    #check errors in delimiters
    def test_should_WrongDelimiter_in_Fun_raise_an_exception(self):
        with self.assertRaises(Exception):
            self.files.makeFilesValues("FUN.BB11001.tsv", "!")

    def test_should_WrongDelimiter_in_Val_raise_an_exception(self):
        with self.assertRaises(Exception):
            self.files.makeFilesSeq("VAR.BB11001.tsv", "*")

    #verify beginnigs of seq files
    def test_should_first_item_of_strik_seq_be_1aab(self):
        strike_seq = open("Best_strike_seq.txt", "r").readlines()
        self.assertEqual("['>1aab_', '']\n", strike_seq[1])

    def test_should_first_item_of_sp_seq_be_1aab(self):
        sp_seq = open("Best_sp_seq.txt", "r").readlines()
        self.assertEqual("['>1aab_', '']\n", sp_seq[1])

    def test_should_first_item_of_tc_seq_be_1aab(self):
        tc_seq = open("Best_tc_seq.txt", "r").readlines()
        self.assertEqual("['>1aab_', '']\n", tc_seq[1])


    #verify specific values of value files
    def test_should_strike_value_of_sp_max_be_199(self):
        sp_seq = open("Best_sp_value.txt", "r").readlines()
        sp_seq_separado = sp_seq[0].split(",")
        self.assertEqual("['1.9975781240868502'", sp_seq_separado[0])

    def test_should_sp_value_of_tc_max_be_837(self):
        sp_tc = open("Best_tc_value.txt", "r").readlines()
        sp_tc_separado = sp_tc[0].split(",")
        self.assertEqual(" '83.7378640776699'", sp_tc_separado[2])

    #verify means
    def test_should_strike_mean_be_2799(self):
        strike_val = open("Best_strike_value.txt", "r").readlines()
        strike_separado = strike_val[1].split(": ")
        self.assertEqual("2.799714601504851", strike_separado[1])

    def test_should_tc_mean_be_2799(self):
        tc_val = open("Best_tc_value.txt", "r").readlines()
        tc_separado = tc_val[1].split(": ")
        self.assertEqual("3.6450563172892525", tc_separado[1])

    def test_should_sp_mean_be_8276(self):
        sp_val = open("Best_sp_value.txt", "r").readlines()
        sp_separado = sp_val[1].split(": ")
        self.assertEqual("82.7642571471821", sp_separado[1])

    def test_should_strike_median_be_288(self):
        strike_val = open("Median_strike_value.txt", "r").readlines()
        self.assertEqual("2.8877640768605", strike_val[0])

    def test_should_tc_median_be_370(self):
        tc_val = open("Median_tc_value.txt", "r").readlines()
        self.assertEqual("3.7037037037037037", tc_val[0])

    def test_should_sp_median_be_829(self):
        sp_val = open("Median_sp_value.txt", "r").readlines()
        self.assertEqual("82.9326923076923", sp_val[0])



if __name__ == '__main__':
    unittest.main()
