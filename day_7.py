
from typing import List


class Equation:
    def __init__(self, test_value: int, numbers = List[int]):
        self.test_value = test_value
        self.numbers = numbers

    def is_valid(self, operators: List[str]) -> bool:
        if len(self.numbers) == 0:
            return False
        if len(self.numbers) == 1:
            return self.numbers[0] == self.test_value
        
        return self.recurse(operators, self.numbers[0])
    
    def recurse(self, operators: List[str], value: int, idx: int = 1) -> bool:
        if idx == len(self.numbers):
            return value == self.test_value
        
        for operator in operators:
            if operator == '+':
                if self.recurse(operators, value + self.numbers[idx], idx + 1):
                    return True
            elif operator == '*':
                if self.recurse(operators, value * self.numbers[idx], idx + 1):
                    return True
            elif operator == '|':
                if self.recurse(operators, int(str(value) + str(self.numbers[idx])), idx + 1):
                    return True
        return False
        

def load_input() -> List[Equation]:
    equations = []
    with open("day_7.txt") as file:
        for line in file:
            line = line.strip()
            test_value, numbers = line.split(":")
            test_value = int(test_value.strip())
            numbers = numbers.strip().split(" ")
            numbers = [int(x) for x in numbers]
            equations.append(Equation(test_value, numbers))
    return equations

def part_1():
    equations = load_input()
    acc = 0
    for equation in equations:
        if equation.is_valid(list('+*')):
            acc += equation.test_value
    print(acc)

def part_2():
    equations = load_input()
    acc = 0
    for equation in equations:
        if equation.is_valid(list('+*|')):
            acc += equation.test_value
    print(acc)

if __name__ == "__main__":
    part_1()
    part_2()
