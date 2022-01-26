class FizzBuzzClass:
    def __init__(self, number):
        self.number = number

    def fizz_or_buss(self):
        result = ""
        result += "Fizz" if self.number % 3 == 0 else ""
        result += "Buzz" if self.number % 5 == 0 else ""
        result = self.number if result == "" else result
        return result
