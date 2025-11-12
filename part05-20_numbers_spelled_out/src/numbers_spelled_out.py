def dict_of_numbers():
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"
    ]
    
    number_dict = {}
    
    for i in range(100):
        if i < 20:
            number_dict[i] = units[i]
        else:
            ten_part = tens[i // 10]
            unit_part = "" if i % 10 == 0 else "-" + units[i % 10]
            number_dict[i] = ten_part + unit_part
    
    return number_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])