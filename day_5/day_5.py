'''
Advent of Code 2024 Day 3: Ceres Search

The description of the puzzle can be found here:
https://adventofcode.com/2024/day/5
'''

from typing import *
from math import floor
import pprint

def parse_input_file(path: str) -> Tuple[Dict[int, List[int]], List[List[int]]]:
    rule_dict: Dict[int, List[int]] = {}
    updates: List[List[int]] = []
    separator_nl_reached: bool = False
    with open(path) as file:
        for line in file:
            stripped: str = line.rstrip()
            if stripped == "":
                separator_nl_reached = True
                continue
            if not separator_nl_reached:
                num_strs = stripped.split("|")
                key = int(num_strs[0])
                value = int(num_strs[1])
                if not rule_dict.get(key):
                    rule_dict[key] = []
                    rule_dict[key].append(value)
                else:
                    rule_dict[key].append(value)
            if separator_nl_reached:
                page_nrs = []
                for num_str in line.split(','):
                    page_nrs.append(int(num_str))
                updates.append(page_nrs)
    return (rule_dict, updates)

def check_position_validity(
    nr1: Tuple[int, int],
    nr2: Tuple[int, int], 
    rules: Dict[int, List[int]]
) -> bool:
    rules_nr2 = rules.get(nr2[0])
    
    if rules_nr2:
        if nr1[0] in rules_nr2:
            return False
    
    return True
    
def check_update_validity(
    update: List[int],
    rules: Dict[int, List[int]],
) -> bool :
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if not check_position_validity((update[i], i), (update[j], j), rules):
                return False
    return True

def sum_correct_updates_middle(
    updates: List[List[int]],
    rules: Dict[int, List[int]]
):
    sum_elems: int = 0
    for update in updates:
        if check_update_validity(update, rules):
            sum_elems += update[len(update) // 2]
    return sum_elems

def order_update_and_return_middle(
    update: List[int],
    rules: Dict[int, List[int]]
) -> Union[int, None]:
    was_incorrect: bool = False
    
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if not check_position_validity((update[i], i), (update[j], j), rules):
                was_incorrect = True
                nr_to_insert = update[j]
                del update[j]
                update.insert(i, nr_to_insert)
    return update[len(update) // 2] if was_incorrect else None

def order_all_updates_sum_incorrects_mid_elems(
    updates: List[List[int]],
    rules: Dict[int, List[int]]
) -> List[int]:
    mid_elem_lst = []
    for update in updates:
        mid_elem = order_update_and_return_middle(update, rules)
        if mid_elem:
            mid_elem_lst.append(mid_elem)
    return sum(mid_elem_lst)
                
if __name__ == "__main__":
    rules, updates = parse_input_file("input.txt")
    
    print(
        "Sum of correctly ordered updates' middle elements: ",
        sum_correct_updates_middle(updates, rules)
    )
    
    print(
        "Sum of all updates middle elements (because now everything is in order): ",
        order_all_updates_sum_incorrects_mid_elems(updates, rules)
    )
    