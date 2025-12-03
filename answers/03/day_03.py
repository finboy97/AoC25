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

###### warning - ugly ugly code, it worked but huge scope to tidy up if had the time

def get_biggest_combo_12_digit(line):
    # put in stack
    # if bigger, pop until reach same, or empty. 
    # if at end, populate with remaining items.
    stack = []
    max_length = 12
    for i in range(len(line)):
        # get the number
        number = line[i]
        # how much is left to the right
        remaining_digits = len(line) - i

        # if the end of the tail is reached then just add everythin on
        if 12 - len(stack) == remaining_digits:
            stack.append(line[i:])
            break

        # empty stack
        if len(stack) == 0:
            stack.append(number)
            continue
        
        # insert if space
        if number <= stack[-1]:
            if len(stack) < 12:
                stack.append(number)

        # reorder
        elif number > stack[-1]:
            inserted = False
            while not inserted:
                stack.pop()

                if len(stack) == 0:
                    stack.append(number)
                    inserted = True
                    continue
                
                if len(stack) == 12 - remaining_digits:
                    stack.append(line[i:])
                    inserted = True
                    return int("".join(stack))

                if number <= stack[-1]:
                    stack.append(number)
                    inserted = True
    return int("".join(stack))

    

with open("data/03/input.txt") as f:
    powerbanks = [x.strip("\n") for x in f.readlines()]
    total_joltage = 0
    for line in powerbanks:
        # print(f"working on line {line}")
        # total_joltage += get_biggest_combo(line)
        # print(get_biggest_combo_12_digit(line))
        total_joltage += get_biggest_combo_12_digit(line)
    print(total_joltage)