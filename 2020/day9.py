from itertools import combinations

def part1(numbers, window):
    init = 0
    end = window
    while end < len(numbers):
        for a, b in combinations(numbers[init: end], 2):
            if (a + b) == numbers[end]:
                break
        else:
            return numbers[end]

        end += 1
        init += 1


def part2(numbers, goal_number):
    print('***********PART 2***************')
    init = 0
    up_index = 1
    
    while init < len(numbers):
        print(numbers[init: up_index])
        current_sum = sum(numbers[init: up_index])
        if current_sum < goal_number:
            up_index += 1
        elif current_sum > goal_number or init == len(numbers):
            init += 1
            up_index = init + 1
        elif current_sum == goal_number:
            subset = numbers[init: up_index]

            return max(subset) + min(subset)
        else:
            raise Exception('Unhandled exception')


if __name__ == "__main__":
    numbers = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    
    assert part1(numbers, 5) == 127
    assert part2(numbers, 127) == 62
    
    with open('2020/day9.txt', 'r') as input_file:
        numbers = [int(l.replace('\n', '')) for l in input_file.readlines()]

    res_part1 = part1(numbers, 25)
    print(f' PART 1: {res_part1}')
    print(f' PART 2: {part2(numbers, res_part1)}')