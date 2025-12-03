# elevators are offline
# escalators are offline
# batteries have a joltage rating from 1 to 9
# batteries are organised into banks - each line of digits is 1 bank
# find the 2 digits in the bank that are highest - add them up. They need to be in order.

# part b - find 12 digits highest

from itertools import combinations

def get_biggest_combo(line):
    biggest = 0
    for x in range(len(line)):
        digit_1 = line[x]
        for y in range(x+1, len(line)):
            number = line[x] + line[y]
            if int(number) > biggest:
                biggest = int(number)
    return biggest


def get_biggest_combo_12_digit(line):
    # pick the -12th character - go backwards, see if anything equal or matches it
    # find highest digit 
    # find leftmost occurrence 
    # if it's within 12 final digits - move on to next highest
    # find next following digits - how to get 
    biggest = 0
    k = 12
    # result = [int(''.join(c)) for c in combinations(line,k)]
    for c in combinations(line, k):
        num = int(''.join(c))
        if num > biggest: biggest = num
    return biggest
        # for x in result:
    #     if int(x) > biggest:
    #         biggest = int(x)
    # return biggest

with open("data/03/input.txt") as f:
    powerbanks = [x.strip("\n") for x in f.readlines()]
    total_joltage = 0
    for line in powerbanks:
        print(f"working on line {line}")
        # total_joltage += get_biggest_combo(line)
        total_joltage += get_biggest_combo_12_digit(line)
    print(total_joltage)