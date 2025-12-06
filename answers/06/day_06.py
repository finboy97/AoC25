import re

pattern = re.compile("\s+")

def get_digits(grid, col, height, string_mode=None):
    digits = []
    for i in range(height-1):
        if string_mode:
            digits.append(grid[i][col])
        else:
            digits.append(int(grid[i][col]))
    return digits


def calculate(grid):
    """
    Take list of lists.
    Get operator off bottom row.
    Get digit for 
    :param grid: list of lists
    """
    height = len(grid)
    width = len(grid[0])

    total = 0

    for col in range(width):
        operator = grid[height-1][col]
        digits = get_digits(grid, col, height)
        if operator == "+":
            # add
            sum = 0
            for num in digits: sum += num
            total += sum
            continue

        elif operator == "*":
            # multiply
            times = digits[0]
            for num in digits[1:]:
                times *= num
            total += times
            continue
        else:
            print("this should not happen")
            continue
    return total


def convert_normal_digits_into_octopod_digits(digits):
    total_numbers = max([len(x) for x in digits])
    new_digits = []
    for i in range(1, total_numbers+1):
        new_digit = ""
        for row in digits:
            try: 
                new_digit = new_digit + row[-i]
            except IndexError:
                continue
        new_digits.append(new_digit)
    return [int(x) for x in new_digits]
                

with open("data/06/test.txt") as f:
    items = []
    for line in f.readlines():
        items.append( pattern.split(line.strip()))
    print(calculate(items))


def do_maths(operator, nums):

    if operator == "+":
        # add
        sum = 0
        for num in nums: sum += num
        return sum       

    elif operator == "*":
        # multiply
        times = nums[0]
        for num in nums[1:]:times *= num
        return times


def calculate_b(input_list):
    """
    Work out the operator.
    Put numbers into a buffer.
    When an empty line is found, this tells us that we can calculate the result for the buffer.
    
    :param input_list: Description
    """

    current_operator = ""
    buffer = []

    total = 0

    for line in input_list:
        if "*" in line:
            # print("multiply", line)
            current_operator = "*"
            buffer.append(int(line.replace("*", "").strip()))
            continue
        elif "+" in line:
            # print("add", line)
            current_operator = "+"
            buffer.append(int(line.replace("+", "").strip()))
            continue
        else:
            stripped = line.strip()
            if len(stripped) == 0:
                # print("do calculation", buffer, current_operator)
                total += (do_maths(current_operator, buffer))
                buffer.clear()
                continue
            else:
                buffer.append(int(stripped))
                continue

    # final calc to use the last buffer:
    total += (do_maths(current_operator, buffer))
    
    return total


# part b - parse differently
with open("data/06/input.txt") as f:
    # flip each column to it's own list item 
    raw_lines = f.readlines()
    longest_line = max(len(line) for line in raw_lines)
    transposed = []
    for i in range(longest_line-1):
        new_line = ""
        for line in raw_lines:
            try:
                new_line += line[i]
            except IndexError:
                new_line += ""
        transposed.append(new_line)
    print(calculate_b(transposed))
