import re

def part1():
    mandatory_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    passport_info = ''
    valid_passports = 0
    with open('2020/day4.txt', 'r') as input_file:
        for str_input in input_file.readlines():
            if str_input == '\n':
                passport_fields = {field.split(':')[0] for field in passport_info.strip().split(' ')}
                mandatories = mandatory_fields.intersection(passport_fields)
                is_valid = len(mandatories) == len(mandatory_fields)
                print(str_input, passport_fields, len(mandatories), is_valid)
                valid_passports += int(is_valid)
                passport_info = ''
            else:
                passport_info += f' {str_input}'
    
        passport_fields = {field.split(':')[0] for field in passport_info.strip().split(' ')}
        mandatories = mandatory_fields.intersection(passport_fields)
        is_valid = len(mandatories) == len(mandatory_fields)
        print(str_input, passport_fields, len(mandatories), is_valid)
        valid_passports += int(is_valid)
        passport_info = ''
        
    return valid_passports

def part2():
    mandatory_dict = {'byr': r"19[2-9][0-9]|200[1-2]", 
                      'iyr': r"201[0-9]|2020", 
                      'eyr': r"202[0-9]|2030", 
                      'hgt': r"1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in", 
                      'hcl': r"#([0-9a-fA-F]{6})", 
                      'ecl': r"amb|blu|brn|gry|grn|hzl|oth", 
                      'pid': r"[0-9]{9}"}
    mandatory_fields = set(mandatory_dict.keys())
    
    passport_info = ''
    valid_passports = 0
    
    with open('2020/day4.txt', 'r') as input_file:
        for str_input in input_file.readlines():
            if str_input == '\n':
                passport_dict = {field.split(':')[0]: field.split(':')[1] 
                                for field in passport_info.strip().split(' ')}
                mandatories = mandatory_fields.intersection(set(passport_dict.keys()))
                is_valid_on_keys = len(mandatories) == len(mandatory_fields)
                
                if is_valid_on_keys:
                    for key in mandatories:
                        if not re.fullmatch(mandatory_dict[key], passport_dict[key].replace('\n', '')):
                            break
                    else:
                        valid_passports += 1
                passport_info = ''
            else:
                passport_info += f' {str_input}'
    
        passport_dict = {field.split(':')[0]: field.split(':')[1] 
                         for field in passport_info.strip().split(' ')}
        mandatories = mandatory_fields.intersection(set(passport_dict.keys()))
        is_valid_on_keys = len(mandatories) == len(mandatory_fields)
        
        if is_valid_on_keys:
            for key in mandatories:
                if not re.fullmatch(mandatory_dict[key], passport_dict[key].replace('\n', '')):
                    break
            else:
                valid_passports += 1
        passport_info = ''
        
    return valid_passports


if __name__ == "__main__":

    print(f' PART 1: {part1()}')
    print(f' PART 2: {part2()}')