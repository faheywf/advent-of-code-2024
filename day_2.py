from typing import List


class Report:
    def __init__(self, levels):
        self.levels: List[int] = levels
        self.max_change = 3
        self.min_change = 1

    def __str__(self):
        return f'Report(levels={self.levels})'
    
    def is_safe(self) -> bool:
        increasing = self.levels[0] < self.levels[1]

        for i in range(len(self.levels)-1):
            current = self.levels[i]
            next = self.levels[i+1]

            diff = abs(current - next)
            if (current == next) or (increasing and current > next) or (not increasing and current < next) or (self.min_change > diff) or (diff > self.max_change):
                return False
        return True
    
    def report_without_idx(self, idx: int) -> 'Report':
        return Report(self.levels[:idx] + self.levels[idx+1:])


def load_input() -> List[Report]:
    reports: List[Report] = []
    with open('day_2.txt') as f:
        for line in f:
            reports.append(Report([int(x) for x in line.strip().split(' ')]))
    return reports

def part_1():
    reports = load_input()
    num_safe_reports = 0

    for report in reports:
        if report.is_safe():
            num_safe_reports += 1
    print(num_safe_reports)

def part_2():
    reports = load_input()
    num_safe_reports = 0

    for report in reports:
        if report.is_safe():
            num_safe_reports += 1
        else:
            # try removing a level with the dampener
            for i in range(len(report.levels)):
                if report.report_without_idx(i).is_safe():
                    num_safe_reports += 1
                    break
    print(num_safe_reports)

if __name__ == '__main__':
    part_1()
    part_2()