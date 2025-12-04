# printing department
# We need to optimise forklift workloads to use them to break through a wall to a canteen (?)
# Rolls of paper (@) are in a grid
# Forklifts can pick up paper if there are fewer than 4 papers in the 8 adjacent positions
# Count all the rolls that can be moved


# part 2
# When a roll can be accessed, remove it from the grid and go again

import sys

def count_moveable_rows(grid):
    grid_length = len(grid)
    grid_width = len(grid[0])

    # moveable_rolls = 0
    moveable_coords = []
    for row in range(grid_length):
        
        for col in range(grid_width):
            adj_rolls = 0
            value = grid[row][col]

            if value in [".","X"]: continue

            # above
            if row > 0:
                # above left
                if col > 0:
                    top_left = grid[row-1][col-1]
                    if top_left == "@": adj_rolls +=1

                # above
                above = grid[row-1][col]
                if above == "@": adj_rolls += 1
                # above right
                if col < grid_width - 1:
                    top_right = grid[row-1][col+1]
                    if top_right == "@": adj_rolls += 1

            # left
            if col > 0:
                left = grid[row][col-1]
                if left == "@": adj_rolls += 1

            # right
            if col < grid_width -1 :
                right = grid[row][col+1]
                if right == "@": adj_rolls += 1
            
            # below
            if row < (grid_length - 1):
                # get below left
                if col > 0:
                    below_left = grid[row+1][col-1]
                    if below_left == "@": adj_rolls += 1
                # get below
                below = grid[row+1][col]
                if below == "@": adj_rolls += 1
                # get below right
                if col < grid_width - 1:
                    below_right = grid[row+1][col+1]
                    if below_right == "@": adj_rolls += 1

            if adj_rolls < 4:
                moveable_coords.append((row, col))
    
    for item in moveable_coords:
        grid[item[0]][item[1]] = "X"
    return moveable_coords, grid

with open("data/04/input.txt") as f:
    grid = [list(x.strip()) for x in f.readlines()]
    moveable_rows, grid = count_moveable_rows(grid)

    total_moved = 0 + len(moveable_rows)
    iteration_num = 0
    while len(moveable_rows) > 0:
        iteration_num += 1
        moveable_rows, grid = count_moveable_rows(grid)
        
        total_moved += len(moveable_rows)
    print(total_moved)