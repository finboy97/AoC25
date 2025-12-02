# looking for invalid product id's in a range of ID's.
# repeated integers are invalid
# 55 , 6464, 123123 for example
# no leading 0
# 0101 isn't an ID, 101 is a valid ID
# objective - find the invalid ID's that appear in the given ranges and sum them together.

# part 2
# anything repeated more than once


def check_for_repeats(start, end):
    repeats = 0
    for num in range(int(start), int(end) + 1):
        str_num = str(num)

        first_half = str_num[0:int(len(str_num)/2)]
        second_half = str_num[int(len(str_num)/2):]
        if first_half == second_half: repeats += int(num)
    return repeats


def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def is_repeated_pattern(str_num, factors):
    for i in range(len(factors)-1):
        slice_len = factors[i]
        num_slice = str_num[:slice_len]
        concat_slice = ""
        for j in range(int(len(str_num)/factors[i])):
            concat_slice = concat_slice + num_slice
        
        if concat_slice == str_num:
            # print("match")
            # print(str_num, slice_len, num_slice, concat_slice)
            return True
    return False


def check_for_repeats_part_2(start, end):
    print("\n", start, end)
    repeats = 0
    for num in range(int(start), int(end) + 1):
        str_num = str(num)
        length_factors = get_factors(len(str_num))
        if is_repeated_pattern(str_num, length_factors):
            repeats += num
    return repeats


def find_bad_ids(id_range_list):
    bad_ids_1 = 0
    for item in id_range_list:
        start = item.split("-")[0]
        end = item.split("-")[1]
        bad_ids_1 += check_for_repeats(start, end)
    return bad_ids_1


def find_bad_ids_part_b(id_range_list):
    bad_ids_1 = 0
    for item in id_range_list:
        start = item.split("-")[0]
        end = item.split("-")[1]
        bad_ids_1 += check_for_repeats_part_2(start, end)
    return bad_ids_1


with open("data/02/input.txt") as f:
    id_ranges = f.readline().split(",")
    # part_a = find_bad_ids(id_ranges)
    part_b = find_bad_ids_part_b(id_ranges)
    print(part_b)
