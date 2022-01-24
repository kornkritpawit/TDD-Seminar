import pytest
from game import FizzBuzzClass


def fizzbuzz(input):
    game = FizzBuzzClass(input)
    return game.fizz_or_buss()


class TestFizzBuzzClass:
    def test_count_1_when_input_is_1(self):
        assert fizzbuzz(1) == 1

    def test_count_2_when_input_is_2(self):
        assert fizzbuzz(2) == 2

    def test_count_fizz_wnen_input_is_3(self):
        assert fizzbuzz(3) == "Fizz"

    def test_count_fizz_when_input_is_4(self):
        assert fizzbuzz(4) == 4

    def test_count_fizz_when_input_is_5(self):
        assert fizzbuzz(5) == "Buzz"

    def test_count_fizz_when_input_is_6(self):
        assert fizzbuzz(6) == "Fizz"

    def test_count_fizz_when_input_is_7(self):
        assert fizzbuzz(7) == 7

    def test_count_fizz_when_input_is_8(self):
        assert fizzbuzz(8) == 8

    def test_count_fizz_when_input_is_9(self):
        assert fizzbuzz(9) == "Fizz"

    def test_count_fizz_when_input_is_10(self):
        assert fizzbuzz(10) == "Buzz"

    def test_count_fizz_when_input_is_11(self):
        assert fizzbuzz(11) == 11

    def test_count_fizz_when_input_is_12(self):
        assert fizzbuzz(12) == "Fizz"

    def test_count_fizz_when_input_is_13(self):
        assert fizzbuzz(13) == 13

    def test_count_fizz_when_input_is_14(self):
        assert fizzbuzz(14) == 14

    def test_count_fizz_when_input_is_15(self):
        assert fizzbuzz(15) == "FizzBuzz"


        
