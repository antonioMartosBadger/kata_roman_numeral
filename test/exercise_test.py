import unittest

from main import convert


class TestExercise(unittest.TestCase):

    def test_given_the_number_1_when_converting_to_roman_then_I_is_returned(self):
        result = convert(1)

        self.assertEqual('I', result)

    def test_given_the_number_2_when_converting_to_roman_then_II_is_returned(self):
        result = convert(2)

        self.assertEqual('II', result)

    def test_given_the_number_3_when_converting_to_roman_then_III_is_returned(self):
        result = convert(3)

        self.assertEqual('III', result)

    def test_given_the_number_4_when_converting_to_roman_then_IV_is_returned(self):
        result = convert(4)

        self.assertEqual('IV', result)

    def test_given_the_number_5_when_converting_to_roman_then_V_is_returned(self):
        result = convert(5)

        self.assertEqual('V', result)

    def test_given_the_number_6_when_converting_to_roman_then_VI_is_returned(self):
        result = convert(6)

        self.assertEqual('VI', result)

    def test_given_the_number_7_when_converting_to_roman_then_VII_is_returned(self):
        result = convert(7)

        self.assertEqual('VII', result)

    def test_given_the_number_8_when_converting_to_roman_then_VIII_is_returned(self):
        result = convert(8)

        self.assertEqual('VIII', result)

    def test_given_the_number_9_when_converting_to_roman_then_IX_is_returned(self):
        result = convert(9)

        self.assertEqual('IX', result)

    def test_given_the_number_10_when_converting_to_roman_then_X_is_returned(self):
        result = convert(10)

        self.assertEqual('X', result)

    def test_given_the_number_11_when_converting_to_roman_then_XI_is_returned(self):
        result = convert(11)

        self.assertEqual('XI', result)

    def test_given_the_number_13_when_converting_to_roman_then_XIII_is_returned(self):
        result = convert(13)

        self.assertEqual('XIII', result)

    def test_given_the_number_14_when_converting_to_roman_then_XIV_is_returned(self):
        result = convert(14)

        self.assertEqual('XIV', result)

    def test_given_the_number_34_when_converting_to_roman_then_XXXIV_is_returned(self):
        result = convert(34)

        self.assertEqual('XXXIV', result)

    def test_given_the_number_19_when_converting_to_roman_then_XIX_is_returned(self):
        result = convert(19)

        self.assertEqual('XIX', result)

