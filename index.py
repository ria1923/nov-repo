class FizzBuzz():
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def play(self):
        for num in range(self.start,self.end):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)
fizzbuzz_game = FizzBuzz(1,101)
