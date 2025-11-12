def line(length, word):
    if word == "":
        print("*" * length)
    else:
        char = word[0]
        print(char * length)

def shape(t_size, t_char, r_size, r_char):
    t_start = 1
    r_start = 0
    while t_start <= t_size:
        line(t_start, t_char)
        t_start += 1
    while r_size > r_start:
        line(t_size, r_char)
        r_start += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 3, "o")