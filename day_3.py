import re


def load_input() -> str:
    daily_input = ""
    with open("day_3.txt") as f:
        for line in f:
            daily_input += line
    return daily_input
    
def part_1():
    daily_input = load_input()
    acc = 0
    # use regex to find all instances of 'mul(x,y)' where x and y are 1-3 digit numbers
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", daily_input):
        x, y = int(match.group(1)), int(match.group(2))
        acc += x * y
    print(acc)

def part_2():
    daily_input = load_input()
    acc = 0

    # remove all text between each 'don't()' and 'do()' instruction
    dont = re.compile(r"don't\(\)")
    do = re.compile(r"do\(\)")
    next_dont = dont.search(daily_input)
    while next_dont:
        next_do = do.search(daily_input[next_dont.end():])
        if next_do:
            daily_input = daily_input[:next_dont.start()] + daily_input[next_dont.end() + next_do.end():]
        else:
            daily_input = daily_input[:next_dont.start()]
        next_dont = dont.search(daily_input)

    # now we do the same thing as in part 1
    # use regex to find all instances of 'mul(x,y)' where x and y are 1-3 digit numbers
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", daily_input):
        x, y = int(match.group(1)), int(match.group(2))
        acc += x * y
    print(acc)

if __name__ == "__main__":
    part_1()
    part_2()