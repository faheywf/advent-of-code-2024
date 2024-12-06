from typing import Dict, List, Tuple


class PageOrderingRule:
    def __init__(self, rule: str):
        self.page_that_must_come_before, self.page_that_must_come_after = rule.split("|")

    def __str__(self):
        return f"{self.page_that_must_come_before} -> {self.page_that_must_come_after}"
    
    def __repr__(self):
        return str(self)
    
class Update:
    def __init__(self, pages: str):
        self.pages: List[str] = pages.split(",")
        self.pages_set = set(self.pages)

    def middle_page(self) -> int:
        return int(self.pages[len(self.pages) // 2])
    
    def ordered_correctly(self, rulebook: Dict[str, List[str]]) -> bool:
        pages_in_update = set()

        for page in self.pages:
            if page in rulebook:
                for prev_page in rulebook[page]:
                    if prev_page in self.pages_set and prev_page not in pages_in_update:
                        return False
            pages_in_update.add(page)

        return True
    
    def fix_order(self, rulebook: Dict[str, List[str]]):
        while not self.ordered_correctly(rulebook):
            # Find the first page that is out of order and move it to the max(indexes of pages that come before it)
            pages_in_update = set()
            for i, page in enumerate(self.pages):
                if page in rulebook:
                    for prev_page in rulebook[page]:
                        if prev_page in self.pages_set and prev_page not in pages_in_update:
                            max_index = max([self.pages.index(prev_page) for prev_page in rulebook[page] if prev_page in self.pages_set])
                            self.pages.pop(i)
                            self.pages.insert(max_index+1, page)
                            break
                pages_in_update.add(page)

    def __str__(self):
        return f"{self.pages}"
    
    def __repr__(self):
        return str(self)
    
def load_input() -> Tuple[List[PageOrderingRule], List[Update]]:
    with open("day_5.txt") as f:
        rules, updates = f.read().split("\n\n")
        rules = [PageOrderingRule(rule) for rule in rules.split("\n")]
        updates = [Update(update) for update in updates.split("\n")]
    return rules, updates

def parse_rules(rules: List[str]) -> Dict[str, List[str]]:
    rulebook : Dict[str, List[str]] = {}
    for rule in rules:
        if rule.page_that_must_come_after not in rulebook:
            rulebook[rule.page_that_must_come_after] = []
        rulebook[rule.page_that_must_come_after].append(rule.page_that_must_come_before)
    return rulebook

def part_1():
    rules, updates = load_input()
    rulebook = parse_rules(rules)

    middle_pages = 0
    for update in updates:
        if update.ordered_correctly(rulebook):
            middle_pages += update.middle_page()

    print(middle_pages)

def part_2():
    rules, updates = load_input()
    rulebook = parse_rules(rules)

    middle_pages = 0
    for update in updates:
        if not update.ordered_correctly(rulebook):
            update.fix_order(rulebook)
            middle_pages += update.middle_page()
    print(middle_pages)

if __name__ == "__main__":
    part_1()
    part_2()