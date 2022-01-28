from leap_year import LeapYear


def leap_year(year):
    game = LeapYear(year)
    return game.is_leap_year()


class TestLeapYearClass:
    def test_century_year_when_input_is_1900(self):
        assert leap_year(1900) == 'century year'

    def test_leap_year_when_input_is_2000(self):
        assert leap_year(2000) == 'leap year'

    def test_leap_year_when_input_is_1996(self):
        assert leap_year(1996) == 'leap year'
    
    def test_leap_year_when_input_is_1997(self):
        assert leap_year(1997) == 'not leap year'
