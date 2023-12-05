import re

conversion_table = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_words(word):
    for k, v in conversion_table.items():
        replaced_word = word.replace(k, v)
    return replaced_word

def calibration(text):
    return sum(int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", text).split("\n"))

data = open("data.txt").read()
print(calibration(data))
print(calibration(replace_words(data)))