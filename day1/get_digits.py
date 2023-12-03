import pdb
import re

sum = 0

with open("data.txt", "r") as my_file:
    data = my_file.readlines()

    for tmp_line in data:
        line = tmp_line.strip("\n")
        digits = re.findall(r'\d', line)
        
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]        
            concat_digits = int("%s%s" % (first_digit, last_digit))
            sum += concat_digits
        
        
pdb.set_trace()

