'''
Advent of Code 2024 Day 1: Historian Hysteria

The description of the puzzle can be found here:
https://adventofcode.com/2024/day/1
'''

from typing import *

def get_lists_distance(lst_a: List, lst_b: List) -> int:
    lst_a.sort()
    lst_b.sort()
    distance = 0
    
    for id_a, id_b in zip(lst_a, lst_b):
        distance += abs(id_a - id_b)
    
    return distance

def get_lists_similarity_score(lst_a: List, lst_b: List) -> int:
    score: int = 0
    
    for number in lst_a:
        score += number * lst_b.count(number)
    
    return score

def parse_numlists_from_file(path: str) -> Tuple[List, List]:
    lst_a: List = []
    lst_b: List = []    
    with open(path) as file:
        for line in file:
            num_strs = line.split()
            lst_a.append(int(num_strs[0]))
            lst_b.append(int(num_strs[1]))
    
    return lst_a, lst_b

if __name__ == "__main__":
    num_lsts = parse_numlists_from_file("day_1_input.txt")
    dist = get_lists_distance(num_lsts[0], num_lsts[1])
    sim_score = get_lists_similarity_score(num_lsts[0], num_lsts[1])
    print(f"Distance between two lists: {dist}")
    print(f"Similarity score: {sim_score}")