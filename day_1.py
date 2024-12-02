from typing import Dict, List, Tuple


def load_input() -> Tuple[List[int], List[int]]:
    left_col, right_col = [], []
    with open('day_1_part_1.txt') as f:
        for line in f:
            left, right = line.split('   ')
            left_col.append(int(left))
            right_col.append(int(right))
    return left_col, right_col

def part_1():
    left_col, right_col = load_input()

    left_col = sorted(left_col)
    right_col = sorted(right_col)

    total_distance = 0
    for i in range(len(left_col)):
        distance = abs(left_col[i] - right_col[i])
        total_distance += distance

    print(total_distance)

def part_2():
    left_col, right_col = load_input()

    right_number_appearance_count: Dict[int, int] = {}
    for right in right_col:
        if right in right_number_appearance_count:
            right_number_appearance_count[right] += 1
        else:
            right_number_appearance_count[right] = 1

    similarity_score = 0
    for left in left_col:
        if left in right_number_appearance_count:
            similarity_score += left * right_number_appearance_count[left]

    print(similarity_score)

if __name__ == '__main__':
    part_1()
    part_2()