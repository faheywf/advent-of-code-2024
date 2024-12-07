
import enum
from typing import List, Set, Tuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        return Point(self.x, self.y - 1)
    
    def down(self):
        return Point(self.x, self.y + 1)
    
    def left(self):
        return Point(self.x - 1, self.y)
    
    def right(self):
        return Point(self.x + 1, self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __repr__(self):
        return f"({self.x}, {self.y})"

class DirectionIndicator(enum.Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

class Guard:
    def __init__(self, location: Point, direction_indicator: str, farthest_point: Point):
        self.location = location
        self.patrolled_points = set()
        self.direction_indicator = DirectionIndicator(direction_indicator)
        self.farthest_point = farthest_point

    def __repr__(self):
        return f"Guard({self.location}, {self.direction_indicator})"

    def is_guard_within_bounds(self) -> bool:
        return 0 <= self.location.x < self.farthest_point.x and 0 <= self.location.y < self.farthest_point.y
    
    def turn(self):
        if self.direction_indicator == DirectionIndicator.UP:
            self.direction_indicator = DirectionIndicator.RIGHT
        elif self.direction_indicator == DirectionIndicator.RIGHT:
            self.direction_indicator = DirectionIndicator.DOWN
        elif self.direction_indicator == DirectionIndicator.DOWN:
            self.direction_indicator = DirectionIndicator.LEFT
        elif self.direction_indicator == DirectionIndicator.LEFT:
            self.direction_indicator = DirectionIndicator.UP

    def patrol(self, obstacles: set[Point]) -> set[Point]:
        while self.is_guard_within_bounds():
            self.patrolled_points.add(self.location)
            if self.direction_indicator == DirectionIndicator.UP:
                next_point = self.location.up()
            elif self.direction_indicator == DirectionIndicator.DOWN:
                next_point = self.location.down()
            elif self.direction_indicator == DirectionIndicator.LEFT:
                next_point = self.location.left()
            elif self.direction_indicator == DirectionIndicator.RIGHT:
                next_point = self.location.right()
            
            if next_point in obstacles:
                self.turn()
            else:
                self.location = next_point
        
        return self.patrolled_points
    
    def will_patrol_forever(self, obstacles) -> bool:
        patrolled_points_with_directions: Set[Tuple[Point, DirectionIndicator]] = set()
        while self.is_guard_within_bounds():
            if (self.location, self.direction_indicator) in patrolled_points_with_directions:
                return True
            
            patrolled_points_with_directions.add((self.location, self.direction_indicator))

            if self.direction_indicator == DirectionIndicator.UP:
                next_point = self.location.up()
            elif self.direction_indicator == DirectionIndicator.DOWN:
                next_point = self.location.down()
            elif self.direction_indicator == DirectionIndicator.LEFT:
                next_point = self.location.left()
            elif self.direction_indicator == DirectionIndicator.RIGHT:
                next_point = self.location.right()
            
            if next_point in obstacles:
                self.turn()
            else:
                self.location = next_point
        return False

    

def load_input() -> Tuple[List[Point], Guard]:
    obstacles = []
    guard_starting_point = None
    farthest_point = Point(0, 0)

    with open("day_6.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c == "#":
                    obstacles.append(Point(x, y))
                elif c == "^" or c == "v" or c == "<" or c == ">":
                    guard_starting_point = Point(x, y)
                    guard_direction = c
                farthest_point = Point(max(farthest_point.x, x), max(farthest_point.y, y))
    return obstacles, Guard(guard_starting_point, guard_direction, farthest_point)

def part_1():
    obstacles, guard = load_input()
    obstacles = set(obstacles)
    patrolled_points = guard.patrol(obstacles)
    print(len(patrolled_points))

def part_2():
    obstacles, guard = load_input()
    obstacles = set(obstacles)
    num_possible_blocked_points = 0
    guard_original_location = guard.location
    guard_original_direction = guard.direction_indicator

    for y in range(guard.farthest_point.y+1):
        for x in range(guard.farthest_point.x+1):
            point = Point(x, y)
            if point not in obstacles and point != guard_original_location:
                # Reset guard location and direction
                guard.location = Point(guard_original_location.x, guard_original_location.y)
                guard.direction_indicator = guard_original_direction

                obstacles.add(point)
                if guard.will_patrol_forever(obstacles):
                    num_possible_blocked_points += 1
                obstacles.remove(point)
    print(num_possible_blocked_points)

if __name__ == "__main__":
    part_1()
    part_2()