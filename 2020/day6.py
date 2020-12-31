def part1(answers):
    res = sum(
        [len(set(ans.replace('\n', ''))) for ans in answers.split('\n\n')]
    )
    
    return res

def part2(answers):
    res = 0
    
    for answer_group in answers.split('\n\n'):
        answer_list = answer_group.split('\n')
        common_answers = set(answer_list[0])
        for ind_answer in answer_list:
            common_answers = common_answers.intersection(set(ind_answer))
            
        res += len(common_answers)

    return res


if __name__ == "__main__":
    
    assert part1('abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb') == 11
    assert part2('abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb') == 6

    with open('2020/day6.txt', 'r') as input_file:
        answers = input_file.read()

    print(f' PART 1: {part1(answers)}')
    print(f' PART 2: {part2(answers)}')
    