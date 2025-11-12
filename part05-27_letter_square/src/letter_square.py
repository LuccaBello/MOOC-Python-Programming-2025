layers = int(input("Layers: "))
size = layers * 2 - 1

for i in range(size):
    for j in range(size):
        layer = max(abs(i - (layers - 1)), abs(j - (layers - 1)))
        letter = chr(ord('A') + layer)
        print(letter, end='')
    print()