def read_fruits():
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.strip()
            name, price = line.split(";")
            fruits[name] = float(price)
    return fruits

if __name__ == "__main__":
    fruit_prices = read_fruits()
    for fruit, price in fruit_prices.items():
        print(f"{fruit}: {price:.2f}")