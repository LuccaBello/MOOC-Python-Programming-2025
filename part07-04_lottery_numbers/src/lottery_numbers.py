from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):

   numbers = range(lower, upper * 1)
   draw = sample(numbers, amount)

   return sorted(draw)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)