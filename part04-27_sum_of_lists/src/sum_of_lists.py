def list_sum(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))