from functools import reduce

def download_tobogan(right: int, down: int):
    trees = 0
    width = 0
    current_x = 0
    # load the map
    with open('2020/day3.txt', 'r') as input_file:
        for i, str_input in enumerate(input_file.readlines()):
            str_input = str_input[:-1]
            if not width:
                width = len(str_input)
                
            if i == 0:
                current_x = current_x + right
                rel_x = current_x - (width * int(current_x / width))
                print(f'{rel_x: 3.0f} - {str_input}')
                print(f'{rel_x: 3.0f} - {(" " * rel_x)}*')
                continue
            
            if i % down != 0:
                print(f'{rel_x: 3.0f} - {str_input}')
                print(f'{rel_x: 3.0f} - {(" " * rel_x)}*')
                continue
            
            # slope down - calculate position
            rel_x = current_x - (width * int(current_x / width))
            whats_in_x = str_input[rel_x]
            
            print(f'{rel_x: 3.0f} - {str_input} -  {whats_in_x} ')
            print(f'{rel_x: 3.0f} - {(" " * rel_x)}*')
            if whats_in_x == '#':
                trees += 1
            
            current_x = current_x + right
                
    return trees

def part1():
    return download_tobogan(right=3, down=1)

def part2():
    steps = [
        download_tobogan(right=1, down=1),
        download_tobogan(right=3, down=1),
        download_tobogan(right=5, down=1),
        download_tobogan(right=7, down=1),
        download_tobogan(right=1, down=2),
    ]
    
    return reduce((lambda x, y: x * y), steps)


if __name__ == "__main__":

    # print(f' PART 1: {part1()}')
    print(f' PART 2: {part2()}')