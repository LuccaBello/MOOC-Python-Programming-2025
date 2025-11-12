def factorials(n: int):
    result = {}
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        result[i] = fact
    return result

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])