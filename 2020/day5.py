import math


ROWS = 128
COLUMNS = 8


def solve_seat(seat: str, rows: int, columns: int):
    current_row = [0, rows -1]
    current_column = [0, columns - 1]
    for n_row in range(7):
        if seat[n_row] == 'F':
            current_row[1] = current_row[1] - math.ceil((current_row[1] - current_row[0]) / 2)
        else:
            current_row[0] = current_row[0] + math.ceil((current_row[1] - current_row[0]) / 2)
    res_row = current_row[0]
    for n_col in range(3):
        if seat[n_row + n_col + 1] == 'L':
            current_column[1] = current_column[1] - math.ceil((current_column[1] - current_column[0]) / 2)
        else:
            current_column[0] = current_column[0] + math.ceil((current_column[1] - current_column[0]) / 2)
    res_col = current_column[0]
        
    result = res_row * 8 + res_col

    return result

def part1(boarding_passes):
    max_id = 0
    
    for boarding_pass in boarding_passes:
        pass_id = solve_seat(boarding_pass, ROWS, COLUMNS)
        if pass_id > max_id:
            max_id = pass_id

    return max_id

def part2(boarding_passes):
    existing_ids = {solve_seat(boarding_pass, ROWS, COLUMNS)
                    for boarding_pass in boarding_passes}
    all_ids = set(range(max(existing_ids)))
    
    missing_ids = all_ids - existing_ids
    
    for board_id in missing_ids:
        if {board_id + 1, board_id - 1}.issubset(existing_ids):
            return board_id


if __name__ == "__main__":
    
    assert part1(['FBFBBFFRLR']) == 357
    assert part1(['BFFFBBFRRR']) == 567
    assert part1(['FFFBBBFRRR']) == 119
    assert part1(['BBFFBBFRLL']) == 820

    with open('2020/day5.txt', 'r') as input_file:
        boarding_passes = [l.replace('\n', '') for l in input_file.readlines()]

    print(f' PART 1: {part1(boarding_passes)}')
    print(f' PART 2: {part2(boarding_passes)}')