from typing import List


def load_input() -> List[List[str]]:
    with open("day_4.txt") as f:
        return [list(line.strip()) for line in f]
    

def part_1():
    word_search = load_input()
    XMAS = ['X', 'M', 'A', 'S']
    X_MIN = 0
    X_MAX = len(word_search[0])
    Y_MIN = 0
    Y_MAX = len(word_search)

    xmas_count = 0

    def search(x: int, y: int, dx: int, dy: int, xmas_idx :int = 0) -> bool:
        searching_for = XMAS[xmas_idx]

        if word_search[y][x] != searching_for:
            return False
        
        if xmas_idx == len(XMAS) - 1:
            return True

        if X_MIN <= x + dx < X_MAX and Y_MIN <= y + dy < Y_MAX:
            if search(x + dx, y + dy, dx, dy, xmas_idx + 1):
                return True
        return False
    
    for y in range(Y_MIN, Y_MAX):
        for x in range(X_MIN, X_MAX):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    if search(x, y, dx, dy):
                        xmas_count += 1

    print(xmas_count)

def part_2():
    word_search = load_input()
    X_MIN = 0
    X_MAX = len(word_search[0])
    Y_MIN = 0
    Y_MAX = len(word_search)
    num_x_mas = 0

    acceptable_corner_patterns = set(['MMSS', 'SSMM', 'MSMS', 'SMSM'])

    for y in range(Y_MIN+1, Y_MAX-1):
        for x in range(X_MIN+1, X_MAX-1):
            if word_search[y][x] == 'A':
                corner_letters = word_search[y-1][x-1] + word_search[y-1][x+1] + word_search[y+1][x-1] + word_search[y+1][x+1]
                if corner_letters in acceptable_corner_patterns:
                    num_x_mas += 1

    print(num_x_mas)

if __name__ == "__main__":
    part_1()
    part_2()