import pdb
import json

def get_winning_numbers(number, winning_numbers):
    if number in winning_numbers:
        return True
    else:
        return False

with open ("data.txt","r") as my_file:
    lines = my_file.readlines()

    cards = dict()

    for line in lines:
        tmp_card = line.split(":")[0].split()[1]
        cards[tmp_card] = 0

        numbers = line.split(":")[1]
        tmp_winning_numbers, tmp_selected_numbers = numbers.split("|")
        winning_numbers = tmp_winning_numbers.split()
        selected_numbers = tmp_selected_numbers.split()

        counter = 0

        for number in selected_numbers:
            is_number_in_winning_numbers = get_winning_numbers(number, winning_numbers)

            if is_number_in_winning_numbers:
                counter += 1

                if counter == 1:
                    cards[tmp_card] += 1
                    
                if counter >1:
                    cards[tmp_card] *= 2
                    

        
        
total_sum = 0

for item in cards:
    total_sum += cards[item]

print(total_sum)


        


