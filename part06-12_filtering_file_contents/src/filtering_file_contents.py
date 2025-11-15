def filter_solutions():
    try:
        with open("solutions.csv", "r") as f_solutions, \
             open("correct.csv", "w") as f_correct, \
             open("incorrect.csv", "w") as f_incorrect:
            
            for line in f_solutions:
                original_line = line
                
                line_stripped = line.strip()
                
                if not line_stripped:
                    continue
                
                try:
                    name, problem, result_str = line_stripped.split(';')
                    
                    correct_result = 0
                    
                    if "+" in problem:
                        operands = problem.split('+')
                        operand1 = int(operands[0])
                        operand2 = int(operands[1])
                        correct_result = operand1 + operand2
                    elif "-" in problem:
                        operands = problem.split('-')
                        operand1 = int(operands[0])
                        operand2 = int(operands[1])
                        correct_result = operand1 - operand2
                    else:
                        continue
                        
                    given_result = int(result_str)
                    
                    if given_result == correct_result:
                        f_correct.write(original_line)
                    else:
                        f_incorrect.write(original_line)
                        
                except (ValueError, IndexError):
                    continue
                    
    except FileNotFoundError:
        print("Error: solutions.csv not found. Please create it first.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    
    sample_data = """Arto;2+5;7
    Pekka;3-2;1
    Erkki;9+3;11
    Arto;8-3;4
    Pekka;5+5;10
    """
    with open("solutions.csv", "w") as f:
        f.write(sample_data)
        
    filter_solutions()
    
    print("--- Contents of correct.csv ---")
    try:
        with open("correct.csv", "r") as f:
            print(f.read().strip())
    except FileNotFoundError:
        print("correct.csv was not created.")

    print("\n--- Contents of incorrect.csv ---")
    try:
        with open("incorrect.csv", "r") as f:
            print(f.read().strip())
    except FileNotFoundError:
        print("incorrect.csv was not created.")