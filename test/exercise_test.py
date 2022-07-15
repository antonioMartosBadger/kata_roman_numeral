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
