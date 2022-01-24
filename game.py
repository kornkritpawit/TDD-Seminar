class FizzBuzzClass():

    def __init__(self, number):
        self.number = number
    
    def fizz_or_buss(self):
        # if self.number == 1:
        #     return self.n
        # elif self.number == 5 or self.number == 10:
        #     return "Buzz"
        # elif self.number == 2: 
        #     return self.number
        # elif self.number == 3 or self.number == 6:
        #     return "Fizz"
        # elif self.number == 4:
        #     return self.number
        # elif self.number == 5:
        #     return "Buzz"
        # elif self.number == 15:
        #     return "FizzBuzz"
        #คือไรนิ
        #ข้างบนคือเทสแบบ ปกติ ข้างล่าง คือ Refac แล้ว
        # %3 = Fizz, %5=Buzz !! ==15 = FizzBuzz
        # test tee
        result = ''

        if self.number % 3 == 0:
           result += 'Fizz'
           
        if self.number % 5 == 0:
            result += 'Buzz'

        if result == '':
            result = self.number

        return result
        