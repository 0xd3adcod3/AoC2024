'''
Advent of Code 2024 Day 3: Mull It Over

The description of the puzzle can be found here:
https://adventofcode.com/2024/day/3
'''

import re as r
from typing import *

'''
    Part 1 of the puzzle
'''
def perform_mul_inst(inst_str: str) -> int:
    extracted_num_strs = inst_str[4:len(inst_str) - 1].split(",")
    return int(extracted_num_strs[0]) * int(extracted_num_strs[1])

def perform_muls(path: str) -> int:
    product_list: List[int] = []
    mul_regex_pattern = r.compile("mul\(\d{1,3},\d{1,3}\)")
    
    with open(path) as file:
        for line in file:
            mul_list = mul_regex_pattern.findall(line)
            for mul_inst in mul_list:
                product_list.append(perform_mul_inst(mul_inst))
    return sum(product_list)

'''
    Part 2 of puzzle
'''
def perform_muls_complex(path: str) -> int:
    inst_regex_pattern = r.compile("mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)")
    can_perform: bool = True
    product_lst: List[int] = []
    
    with open(path) as file:
        for line in file:
            inst_lst = inst_regex_pattern.findall(line)
            for inst in inst_lst:
                if inst == "don\'t()": can_perform = False
                if inst == "do()": can_perform = True
                if inst.startswith("mul") and can_perform:
                    product_lst.append(perform_mul_inst(inst))
    
    return sum(product_lst)
                    

if __name__ == "__main__":
    print('Part 1 of the puzzle: {}'.format(perform_muls("input.txt")))
    print('Part 2 of the puzzle: {}'.format(perform_muls_complex("input.txt")))