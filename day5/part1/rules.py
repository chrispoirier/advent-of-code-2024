from typing import List

class rule:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def validate(self, value: List[int]):
        return value.index(self.first) < value.index(self.second)
    
    def string(self):
        return f"{self.first} < {self.second}"

class rules:
    def __init__(self, data):
        self.rules: List[rule] = []
        for line in data:
            line = line.split('|')
            self.rules.append(rule(int(line[0]), int(line[1])))
    
    def get_rules_by_all(self, value: List[int]):
        myRules = rules([])
        for r in self.rules:
            if r.first in value and r.second in value:
                myRules.append(r)
        return myRules
    
    def append(self, rule):
        self.rules.append(rule)

    def validate(self, value: List[int]):
        allValid = True
        for r in self.rules:
            allValid = allValid and r.validate(value)
        return allValid
        