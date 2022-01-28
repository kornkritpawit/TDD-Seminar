class LeapYear:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        if self.year % 100 == 0:
            if self.year % 400 == 0:
                return 'leap year'
            else:
                return 'century year'
        elif self.year % 4 == 0:
            return 'leap year'
