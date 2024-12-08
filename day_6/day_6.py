from __future__ import annotations
from typing import *

class Vector2():
    
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y
    
    def __add__(self, other_vec: Vector2) -> Vector2:
        return Vector2(self.x + other_vec.x, self.y + other_vec.y)
    
    def __repr__(self) -> str:
        return f"{self.x= } {self.y= }"
    
    def __eq__(self, other: Vector2) -> bool:
        return self.x == other.x and self.y == other.y
    
class Directions:
    
    UP: Vector2 = Vector2(0, -1)
    RIGHT: Vector2 = Vector2(1, 0)
    DOWN: Vector2 = Vector2(0, 1)
    LEFT: Vector2 = Vector2(-1, 0)

class Map():
    
    class Element():
        OBSTACLE: str = "#"
        FREE: str = "."
        VISITED: str = "X"
        GUARDUP: str = "^"
        GUARDDOWN: str = "v"
        GUARDLEFT: str = "<"
        GUARDRIGHT: str = ">"
    
    def __init__(self, path):
        self.__data: List[List[Map.Element]] = self.__load(path)
        
    def __load(self, path):
        data: List[List[str]] = []
        with open(path) as file:
            for line in file:
                data.append(list(line.rstrip()))
        return data
    
    def get_guard(self) -> Guard:
        pos: Vector2 = None
        dir: Vector2 = None
        guard_elems = (Map.Element.GUARDDOWN, Map.Element.GUARDLEFT, Map.Element.GUARDRIGHT, Map.Element.GUARDUP)
        for i in range(len(self.__data) - 1):
            for j in range(len(self.__data[0]) - 1):
                map_el = self.__data[i][j]
                if map_el in guard_elems:
                    pos = Vector2(j, i)
                    if map_el == Map.Element.GUARDUP:
                        dir = Directions.UP
                    if map_el == Map.Element.GUARDRIGHT:
                        dir = Directions.RIGHT
                    if map_el == Map.Element.GUARDDOWN:
                        dir = Directions.DOWN
                    if map_el == Map.Element.GUARDLEFT:
                        dir = Directions.LEFT
        return Guard(pos, dir)
        
    def get_map_elem(self, pos: Vector2) -> Map.Element:
        return self.__data[pos.y][pos.x]
    
    def set_map_elem(self, pos: Vector2, elem: Map.Element) -> None:
        if self.is_valid_pos(pos):
            self.__data[pos.y][pos.x] = elem
    
    def is_valid_pos(self, pos: Vector2) -> bool:
        y_size = len(self.__data)
        x_size = len(self.__data[0])
        return pos.x < x_size and pos.x >= 0 and pos.y < y_size and pos.y >= 0
    
    def __repr__(self):
        return "\n".join(["".join(s) for s in self.__data])

class Guard:
    
    def __init__(self, pos: type[Vector2], dir: type[Vector2]):
        self.pos: Vector2 = pos
        self.dir: Vector2 = dir
        self.step_count: int = 0
    
    def traverse_map(self, map: type[Map]) -> None:
        new_pos: Vector2 = self.pos + self.dir
        
        visitable: Tuple[Map.Element] = (
            Map.Element.FREE,
            Map.Element.VISITED,
            Map.Element.GUARDUP,
            Map.Element.GUARDDOWN,
            Map.Element.GUARDLEFT,
            Map.Element.GUARDRIGHT
        )
        
        while(map.is_valid_pos(new_pos)):
            next_map_elem = map.get_map_elem(new_pos)
            
            if  next_map_elem in visitable:
                if next_map_elem != Map.Element.VISITED:
                    self.step_count += 1
                
                old_pos = self.pos
                self.pos = new_pos
                
                map.set_map_elem(old_pos, Map.Element.VISITED)
                map.set_map_elem(new_pos, self.__get_guard_char())
                
            if next_map_elem == Map.Element.OBSTACLE:
                self.__turn_right()
                map.set_map_elem(self.pos, self.__get_guard_char())
                
            new_pos = self.pos + self.dir
            
            if not map.is_valid_pos(new_pos):
                map.set_map_elem(self.pos, Map.Element.VISITED)
                self.step_count += 1
    
    def __get_guard_char(self) -> str:
        if self.dir == Directions.UP:
            return "^"
        elif self.dir == Directions.RIGHT:
            return ">"
        elif self.dir == Directions.DOWN:
            return "v"
        else:
            return "<"
    
    def __turn_right(self) -> None:
        if self.dir == Directions.UP:
            self.dir = Directions.RIGHT
        elif self.dir == Directions.RIGHT:
            self.dir = Directions.DOWN
        elif self.dir == Directions.DOWN:
            self.dir = Directions.LEFT
        elif self.dir == Directions.LEFT:
            self.dir = Directions.UP

if __name__ == "__main__":
    m = Map("input.txt")
    g = m.get_guard()
    g.traverse_map(m)
    print(m)
    print(g.step_count)
