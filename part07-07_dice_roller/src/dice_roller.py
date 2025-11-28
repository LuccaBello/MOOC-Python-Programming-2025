import random

def roll(die: str):
    sides = []
    if die == "A":
        sides = [3, 3, 3, 3, 3, 6]
    elif die == "B":
        sides = [2, 2, 2, 5, 5, 5]
    elif die == "C":
        sides = [1, 4, 4, 4, 4, 4]
    else:
        raise ValueError("Invalid die type. Use 'A', 'B' or 'C'.")

    return random.choice(sides)

def play(die1: str, die2: str, times: int):
    wins1 = 0
    wins2 = 0
    ties = 0

    for _ in range(times):
        result1 = roll(die1)
        result2 = roll(die2)

        if result1 > result2:
            wins1 += 1
        elif result2 > result1:
            wins2 += 1
        else:
            ties += 1
    
    return (wins1, wins2, ties)

if __name__ == "__main__":
    print("Rolling die A 20 times:")
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    
    print("Rolling die B 20 times:")
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    
    print("Rolling die C 20 times:")
    for i in range(20):
        print(roll("C"), " ", end="")
    print("\n")
        
    result = play("A", "C", 1000)
    print(f"Play A vs C (1000 times): {result}")
    
    result = play("B", "B", 1000)
    print(f"Play B vs B (1000 times): {result}")