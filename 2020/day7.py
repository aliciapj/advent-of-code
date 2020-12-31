import re
from collections import defaultdict


def part1(rules):
    form_rules = rules.split('\n')
    
    # build the rules dict: 
    # {bag_name: list of bag that contains it}
    rule_dict = defaultdict(list)
    for rule in form_rules:
        if not rule:
            continue
        split_rules = rule.split(' contain ')
        raw_rules = [re.findall(r'([1-9]|no) (?s)(.*) bag', raw_rule) 
                            for raw_rule in split_rules[1].split(', ')]
        
        for regex_rule in raw_rules:
            rule_dict[regex_rule[0][1]].append(split_rules[0].replace(' bags', ''))

    # process the rules:
    # 1 bag name required - bags that contains it
    colors_to_search = {'shiny gold'}
    res_set = set()
    while colors_to_search:
        new_colors = []
        for color in colors_to_search:
            new_colors += rule_dict[color]
        
        new_color_set = set(new_colors)
        colors_to_search = new_color_set - res_set
        res_set = res_set.union(new_color_set)
    
    return len(res_set)

def _inside_the_bag(rule_dict, bag_name, bags_count) -> int:

    if rule_dict[bag_name] == [('no', 'other')]:
        return bags_count
    else:
        for rule in rule_dict[bag_name]:
            bags_count += int(rule[0]) + int(rule[0]) * _inside_the_bag(rule_dict, rule[1], 0)

    return bags_count

def part2(rules):
    
    form_rules = rules.split('\n')
    
    # build the rules dict: 
    # {bag_name: list of bags inside}
    rule_dict = {}
    
    for rule in form_rules:
        if not rule:
            continue
        split_rules = rule.split(' contain ')
        raw_rules = [re.findall(r'([1-9]|no) (?s)(.*) bag', raw_rule) 
                            for raw_rule in split_rules[1].split(', ')]
        
        rule_dict[split_rules[0].replace(' bags', '')] = \
            [regex_rule[0] for regex_rule in raw_rules]

    # process the rules:
    # 1 bag name required - bags that contains in the inside
    # Warning! recursion inside :)
    bag_count = _inside_the_bag(rule_dict, 'shiny gold', 0)
    
    return bag_count



if __name__ == "__main__":
    
    test1 = (
        'light red bags contain 1 bright white bag, 2 muted yellow bags.\n'
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n'
        'bright white bags contain 1 shiny gold bag.\n'
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n'
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n'
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n'
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n'
        'faded blue bags contain no other bags.\n'
        'dotted black bags contain no other bags.'
    )
    
    assert part1(test1) == 4
    assert part2(test1) == 32

    with open('2020/day7.txt', 'r') as input_file:
        rules = input_file.read()

    print(f' PART 1: {part1(rules)}')
    print(f' PART 2: {part2(rules)}')