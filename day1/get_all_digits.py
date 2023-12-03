import pdb
import re

def convert_to_digit(digit_text):    
    conversion_table = {}
    conversion_table["one"] = 1
    conversion_table["two"] = 2
    conversion_table["three"] = 3
    conversion_table["four"] = 4
    conversion_table["five"] = 5
    conversion_table["six"] = 6
    conversion_table["seven"] = 7
    conversion_table["eight"] = 8
    conversion_table["nine"] = 9

    conversion_table["1"] = 1
    conversion_table["2"] = 2
    conversion_table["3"] = 3
    conversion_table["4"] = 4
    conversion_table["5"] = 5
    conversion_table["6"] = 6
    conversion_table["7"] = 7
    conversion_table["8"] = 8
    conversion_table["9"] = 9

    return conversion_table.get(digit_text, None)

total_sum = 0

with open("data.txt", "r") as my_file:
    data = my_file.readlines()

    for tmp_line in data:
        line = tmp_line.strip("\n")
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line)
        
        if digits:                        
            first_digit = convert_to_digit(digits[0])
            last_digit = convert_to_digit(digits[-1]) 

            if first_digit is not None and last_digit is not None:                       
                concat_digits = int(f"{first_digit}{last_digit}")
                total_sum += concat_digits
            
        
        
pdb.set_trace()

