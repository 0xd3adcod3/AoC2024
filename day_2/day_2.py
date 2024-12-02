'''
Advent of Code 2024 Day 2: Red Nosed Reports

The description of the puzzle can be found here:
https://adventofcode.com/2024/day/2
'''

from typing import *

'''
    Checks whether the given list of levels (the report) safe or not
    
    level_lst: list of ints representing levels
'''
def check_safety(level_lst: List[int]) -> bool:
    diff = level_lst[0] - level_lst[1]
    abs_diff = abs(diff)
    if diff == 0 or abs_diff > 3 or abs_diff < 1:
        return False
    
    for i in range(1, len(level_lst) - 1):
        act_diff = level_lst[i] - level_lst[i + 1]
        if diff < 0 and act_diff >= 0 or diff > 0 and act_diff <= 0:
            return False
        
        abs_act_diff = abs(act_diff)
        if abs_act_diff > 3 or abs_act_diff < 1:
            return False
            
    return True

'''
    Given a list of reports counts and returns the number of safe ones
    
    path: input file name, which contains the reports. Each number is separated
          by space and each report is separated by '\n'  
'''
def count_safe_reports(path: str) -> int:
    safe_reports_count = 0
    
    with open(path) as file:
        for line in file:
            level_lst = [int(num) for num in line.split()]
            if check_safety(level_lst):
                safe_reports_count += 1
    
    return safe_reports_count

'''
    Second part of the challenge. Brute force solution.
'''
def count_safe_reports_dampened(path: str) -> int:
    safe_reports_count = 0
    
    with open(path) as file:
        for line in file:
            level_lst = [int(num) for num in line.split()]
            if check_safety(level_lst):
                safe_reports_count += 1
            elif problem_dampener(level_lst):
                safe_reports_count += 1
    
    return safe_reports_count

def problem_dampener(level_lst: List[int]) -> bool:
    for i in range(len(level_lst)):
        actual_list = [num for j, num in enumerate(level_lst) if j != i]
        if check_safety(actual_list):
            return True
    return False

if __name__ == "__main__":
    print(f"Safe reports: {count_safe_reports('input.txt')}")
    print(f"Safe reports with problem dampener: {count_safe_reports_dampened('input.txt')}")