from itertools import combinations
from collections import Counter


def part1():
    with open('day2.txt', 'r') as input_file:
        valid = 0
        for str_input in input_file.readlines():
            number_of_times, letter, password = str_input.replace(':', '').split(' ')
            min_times, max_times = number_of_times.split('-')

            if int(min_times) <= Counter(password).get(letter, 0) <= int(max_times):
                valid +=1
    return valid


def part2():
    
    with open('day2.txt', 'r') as input_file:
        valid = 0
        for str_input in input_file.readlines():
            number_of_times, letter, password = str_input.replace(':', '').split(' ')
            min_times, max_times = number_of_times.split('-')
            min_times, max_times = int(min_times), int(max_times)
            
            letter_in_1st = password[min_times - 1] == letter
            letter_in_2nd = password[max_times - 1] == letter 
            
            if (letter_in_1st and not letter_in_2nd) or (not letter_in_1st and letter_in_2nd):
                valid += 1
    return valid


if __name__ == "__main__":

    print(f' PART 1: {part1()}')
    print(f' PART 2: {part2()}')