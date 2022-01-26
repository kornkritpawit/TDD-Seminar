from leap_year import LeapYear


def leap_year(year):
    game = LeapYear(year)
    return game.is_leap_year()


class TestLeapYearClass:
    def test_true_when_input_is_2000(self):
        assert leap_year(2000) is True
