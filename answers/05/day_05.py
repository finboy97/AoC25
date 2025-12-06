# The database uses ingredient IDs - it has a list of ID ranges, a blank line and a list of available ingredient ID's
# ID rangse are inclusive
# Ranges can overlap
# How many of the available ingredient IDs are fresh?


def count_fresh_ingredients(ranges, ids):
    fresh_count = 0
    range_list = [x.split("-") for x in ranges]
    for id in ids:
        for item in range_list:
            if int(id) >= int(item[0]) and int(id) <= int(item[1]):
                fresh_count += 1
                break
        
    return fresh_count

    
# part 2
# How many ingredient ID's are considered to be fresh
# Don't care about the individual ID's - want to count the ranges

# new range cases:
# range within existing range: nothing
# range encompasses existing range: delete existing range
# range start within existing range and end outside of any range: extend the end of the existing range
# range start outside of any range and end within existing range: extend the start of the existing range
# structures -> Tree, linkedlist?

def part_b(ranges):
    """ 
    Unoriginal idea - I didn't think of sorting by range start until I saw someone else do it. The logic is my own
    """
    # Step 1: sort ranges by start
    ranges_split = []
    for item in ranges:
        ranges_split.append([int(x) for x in item.split("-")])

    ranges_split.sort(key=lambda x: x[0])

    print(ranges_split)

    merged_ranges = []

    for item in ranges_split:
        if len(merged_ranges) == 0:
            merged_ranges.append(item)
            continue
        # check for overlap of -1 end and current start
        if merged_ranges[-1][1] >= item[0]:
            # current within range of -1 fully - drop it
            if item[1] <= merged_ranges[-1][1]:
                continue
            # else set -1 end to current end
            merged_ranges[-1][1] = item[1]
            continue
        
        # if no overlap then just append to list
        merged_ranges.append(item)

    total_ids = 0

    for x in merged_ranges:
        total_ids += ((x[1] - x[0]) +1)

    print(total_ids)




with open("data/05/input.txt") as f:
    ranges = []
    ids = []
    skipped = False
    for line in [x.strip() for x in f.readlines()]:
        if len(line) == 0:
            skipped = True
            continue
        if not skipped:
            ranges.append(line)
        else:
            ids.append(line)

    # print(count_fresh_ingredients(ranges, ids))
    part_b(ranges)

    