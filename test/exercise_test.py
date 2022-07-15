import unittest

from main import convert


class TestExercise(unittest.TestCase):

    def test_given_the_number_1_when_converting_to_roman_then_I_is_returned(self):
        result = convert(1)

        self.assertEqual('I', result)

    def test_given_the_number_2_when_converting_to_roman_then_II_is_returned(self):
        result = convert(2)

        self.assertEqual('II', result)
