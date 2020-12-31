from typing import Tuple
from copy import deepcopy


def _run_instructions(instructions:dict) -> Tuple[int, bool]:

    executed_index = []
    current_index = 0
    accum = 0

    while current_index not in executed_index and current_index in instructions:
        operator, arg = instructions[current_index]
        arg = int(arg)
        executed_index.append(current_index)

        if operator == 'acc':
            accum += arg
            current_index += 1
        elif operator == 'nop':
            current_index += 1
        elif operator == 'jmp':
            current_index += arg
        else:
            raise Exception(f'Operator {operator} not supported')

    inf_loop = (current_index in executed_index)

    return accum, inf_loop

def part1(code):
    # build a dictionary with instructions:
    # {line_index: [operator, argument]}
    instructions = {index: line.split(' ') 
                    for index, line in enumerate(code.split('\n'))}
    accum, inf_loop = _run_instructions(instructions)

    return accum

def part2(code):
    # build a dictionary with instructions:
    # {line_index: [operator, argument]}
    nop_jmp_idx = []
    instructions = {}

    for index, line in enumerate(code.split('\n')):
        instructions[index] = line.split(' ')
        if instructions[index][0] in ('nop', 'jmp'):
            nop_jmp_idx.append(index)

    # perform switch and test new paths only in nop_jmp_idx
    for idx_tbc in nop_jmp_idx:
        new_inst = deepcopy(instructions)
        old_op, old_arg = instructions[idx_tbc]
        new_op = 'nop' if old_op == 'jmp' else 'jmp'
        new_inst[idx_tbc] = [new_op, old_arg]

        accum, inf_loop = _run_instructions(new_inst)

        if not inf_loop:
            return accum


if __name__ == "__main__":

    test1 = (
        'nop +0\n'
        'acc +1\n'
        'jmp +4\n'
        'acc +3\n'
        'jmp -3\n'
        'acc -99\n'
        'acc +1\n'
        'jmp -4\n'
        'acc +6'
    )

    assert part1(test1) == 5
    assert part2(test1) == 8

    with open('2020/day8.txt', 'r') as input_file:
        code = input_file.read().strip()

    print(f' PART 1: {part1(code)}')
    print(f' PART 2: {part2(code)}')