'''
Advent of Code 2024 Day 3: Ceres Search

The description of the puzzle can be found here:
https://adventofcode.com/2024/day/4
'''

from typing import *

def is_valid_pos(matrix: List[List[str]], pos: Tuple[int, int]) -> bool:
    mat_size_x = len(matrix[0])
    mat_size_y = len(matrix)
    
    pos_x, pos_y = pos
    
    if pos_x < 0 or pos_x >= mat_size_x or pos_y < 0 or pos_y >= mat_size_y:
        return False
    
    return True

def match_word_in_direction(
    matrix: List[List[str]],
    pos: Tuple[int, int],
    dir: Tuple[int, int],
    word: str
) -> int:
    
    if len(word) == 0:
        return 1
    
    if not is_valid_pos(matrix, pos):
        return 0
    
    x, y = pos
    dx, dy = dir
    
    if matrix[y][x] == word[0]:
        return match_word_in_direction(matrix, (x + dx, y + dy), dir, word[1:])
    else: 
        return 0

def match_word_all_dirs(
    matrix: List[List[str]],
    pos: Tuple[int, int],
    word: str
) -> int:
    dirs = (
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),           (1, 0),
        (-1, 1), (0, 1), (1, 1)
    )
    
    count: int = 0
    
    for dir in dirs:
        count += match_word_in_direction(matrix, pos, dir, word)

    return count
    
def search_all_word_occurences_in_matrix(
    matrix: List[List[str]],
    word: str
) -> int:
    sum_of_occs = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == word[0]:
               sum_of_occs += match_word_all_dirs(matrix, (j, i), word)
    
    return sum_of_occs

def search_x_mass_occurences(matrix: List[List[str]]) -> int:
    count: int = 0
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            if matrix[i][j] == "S" or matrix[i][j] == "M":
                if match_word_in_direction(matrix, (j, i), (1, 1), "SAM") or match_word_in_direction(matrix, (j, i), (1, 1), "MAS"):
                    if match_word_in_direction(matrix, (j + 2, i), (-1, 1), "SAM") or match_word_in_direction(matrix, (j + 2, i), (-1, 1), "MAS"):
                        count += 1
                        continue

    return count
        
def parse_input_file(path: str) -> List[List[str]]:
    mat: List[List[str]] = []
    with open(path) as file:
        for line in file:
            mat.append(list(line.rstrip()))
    return mat

if __name__ == "__main__":
    input_mat = parse_input_file("input.txt")
    print("All XMAS occurences in the letter matrix: ", search_all_word_occurences_in_matrix(input_mat, "XMAS"))
    print("All X-MAS occurences in the letter matrix: ", search_x_mass_occurences(input_mat))