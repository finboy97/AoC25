# teleporter, tachyon beam, something or other

def get_below(grid, row, col, side=None):
    if not side:
        return grid[row+1][col]
    if side == "L":
        try:
            return grid[row+1][col-1]
        except IndexError:
            return None
    elif side == "R":
        try:
            return grid[row+1][col+1]
        except IndexError:
            return None



def count_beams_a(grid):
    total_splits = 0
    width = len(grid[0])
    for row in range(len(grid) - 1):
        for col in range(width-1):
            col_val = grid[row][col]
            if col_val == ".":
                continue
            elif col_val == "S":
                grid[row+1][col] = "|"
            elif col_val == "|":
                below = get_below(grid, row, col)
                if below == ".":
                    grid[row+1][col] = "|"
                elif below == "^":
                    below_left = get_below(grid, row, col, "L")
                    below_right = get_below(grid, row, col, "R")
                    split = False
                    if below_left:
                        if below_left == ".":
                            grid[row+1][col-1] = "|"
                            split = True
                    if below_right:
                        if below_right == ".":
                            grid[row+1][col+1] = "|"
                            split = True
                    if split:
                        total_splits += 1
    
    print(total_splits)
    print(count_beams(grid))


def count_beams(grid):
    total_beams = 0
    for row in grid:
        print(row)
        for item in row:
            if item == "|":
                total_beams += 1
    return total_beams


def turn_grid_into_state(grid):
    state = "".join(["".join(x) for x in grid])
    print(state)




def count_multiverses(grid):
    width = len(grid[0])

    states_stack = []
    visited_states = set()

    for row in range(len(grid) - 1):
        for col in range(width-1):
            col_val = grid[row][col]
            if col_val == ".":
                continue
            elif col_val == "S":
                grid[row+1][col] = "|"
                states_stack.append(turn_grid_into_state(grid))
            elif col_val == "|":
                below = get_below(grid, row, col)
                if below == ".":
                    grid[row+1][col] = "|"
                elif below == "^":
                    below_left = get_below(grid, row, col, "L")
                    below_right = get_below(grid, row, col, "R")
                    split = False
                    if below_left:
                        if below_left == ".":
                            grid[row+1][col-1] = "|"
                            states_stack.append(grid)
                            split = True
                    if below_right:
                        if below_right == ".":
                            grid[row+1][col+1] = "|"
                            split = True
                   




with open("data/07/testt.txt") as f:
    grid = [list(x.strip()) for x in  f.readlines()]
    # count_beams_a(grid)
    count_multiverses(grid)

