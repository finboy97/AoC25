def left_turn(start, ticks, circle_size):
    # wrap using modulo so negative results are handled correctly
    return (start - ticks) % circle_size

def right_turn(start, ticks, circle_size):
    # wrap using modulo; don't hard-code 99
    return (start + ticks) % circle_size

def get_zero_ticks(data, start, circle_size):
    zero_ticks = 0
    current = start
    for line in data:
        print(current, line)
        direction = line[0]
        ticks = int(line[1:])
        if direction == "L":
            current = left_turn(current, ticks, circle_size)
        elif direction == "R":
            current = right_turn(current, ticks, circle_size)
        if current == 0:
            zero_ticks += 1
    return zero_ticks


def b_left_turn(start, ticks, circle_size):
    # number of times 0 is hit while moving left by `ticks` from `start`
    offset = circle_size - start if start != 0 else 0
    passes = (ticks + offset) // circle_size
    result = (start - ticks) % circle_size
    return result, passes

def b_right_turn(start, ticks, circle_size):
    # number of times 0 is hit while moving right by `ticks` from `start`
    offset = start if start != 0 else 0
    passes = (ticks + offset) // circle_size
    result = (start + ticks) % circle_size
    return result, passes

def b_get_zero_ticks(data, start, circle_size):
    zero_ticks = 0
    current = start
    for line in data:
        print(current, line)
        direction = line[0]
        ticks = int(line[1:])
        if direction == "L":
            current, passes = b_left_turn(current, ticks, circle_size)
            zero_ticks += passes
        elif direction == "R":
            current, passes = b_right_turn(current, ticks, circle_size)
            zero_ticks += passes
    return zero_ticks



with open("data/01/input.txt") as f:
    data = [x.strip("\n") for x in f.readlines()]
    print(data)

    start = 50
    circle_size = 100
    # print(get_zero_ticks(data, start, circle_size))
    print(b_get_zero_ticks(data, start, circle_size))