import string

def run(program):
    variables = {char: 0 for char in string.ascii_uppercase}
    
    labels = {}
    for i, line in enumerate(program):
        if line.endswith(":"):
            label_name = line[:-1]
            labels[label_name] = i
            
    printed_values = []
    pc = 0 
    n = len(program)
    
    def get_value(token):
        if token in variables:
            return variables[token]
        else:
            return int(token)
            
    while pc < n:
        line = program[pc]
        parts = line.split()
        command = parts[0]
        
        if command == "PRINT":
            val = get_value(parts[1])
            printed_values.append(val)
            pc += 1
            
        elif command == "MOV":
            target_var = parts[1]
            val = get_value(parts[2])
            variables[target_var] = val
            pc += 1
            
        elif command == "ADD":
            target_var = parts[1]
            val = get_value(parts[2])
            variables[target_var] += val
            pc += 1
            
        elif command == "SUB":
            target_var = parts[1]
            val = get_value(parts[2])
            variables[target_var] -= val
            pc += 1
            
        elif command == "MUL":
            target_var = parts[1]
            val = get_value(parts[2])
            variables[target_var] *= val
            pc += 1
            
        elif command == "JUMP":
            location = parts[1]
            pc = labels[location]
            
        elif command == "IF":
            val1 = get_value(parts[1])
            op = parts[2]
            val2 = get_value(parts[3])
            location = parts[5]
            
            condition_met = False
            if op == "==":
                condition_met = (val1 == val2)
            elif op == "!=":
                condition_met = (val1 != val2)
            elif op == "<":
                condition_met = (val1 < val2)
            elif op == "<=":
                condition_met = (val1 <= val2)
            elif op == ">":
                condition_met = (val1 > val2)
            elif op == ">=":
                condition_met = (val1 >= val2)
                
            if condition_met:
                pc = labels[location]
            else:
                pc += 1
                
        elif command == "END":
            break
            
        elif command.endswith(":"):
            pc += 1
            
        else:
            pc += 1
            
    return printed_values

if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)