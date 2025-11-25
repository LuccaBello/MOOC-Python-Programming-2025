from fractions import Fraction
def fractionate(amount: int):

    return [Fraction(1, amount)] * amount

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))