from datetime import datetime

def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    date_part = pic[:6]
    century = pic[6]
    personal_id = pic[7:10]
    control_digit = pic[10]

    century_map = {'+': 1800, '-': 1900, 'A': 2000}
    if century not in century_map:
        return False

    try:
        day = int(date_part[:2])
        month = int(date_part[2:4])
        year = int(date_part[4:6])

        full_year = century_map[century] + year

        datetime(full_year, month, day)
    
    except ValueError:
        return False

    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    try:
        digit_str = date_part + personal_id
        digit_num = int(digit_str)

        remainder = digit_num % 31

        if control_string[remainder] != control_digit:
            return False

    except ValueError:
        return False
    
    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L")) 
    print(is_it_valid("310823A9877")) 
    print(is_it_valid("320823A9877")) 
    print(is_it_valid("230827-906G")) 
