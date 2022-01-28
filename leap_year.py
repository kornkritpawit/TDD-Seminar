class LeapYear:
    def __init__(self, year):
        self.year = year

    def is_leap_year(self):
        if self.year % 100 == 0:
            return 'century year'
