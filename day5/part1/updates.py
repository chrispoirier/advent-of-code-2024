from typing import List
from rules import rules

class update:
    def __init__(self, line):
        self.pages: List[int] = []
        for page in line.split(','):
            self.pages.append(int(page))

    def is_valid(self, rulesObj: rules):
        myRules = rulesObj.get_rules_by_all(self.pages)
        #print([r.string() for r in myRules.rules])
        return myRules.validate(self.pages)

class updates:
    def __init__(self, data):
        self.updates: List[update] = []
        for line in data:
            self.updates.append(update(line))

    def get_valid_updates(self, rulesObj: rules):
        validUpdates = updates([])
        for u in self.updates:
            #print(u.pages)
            if u.is_valid(rulesObj):
                #print("valid")
                validUpdates.append(u)
                #print([u.pages for u in validUpdates.updates])
            #else:
                #print("invalid")
            #print("----")
        return validUpdates
    
    def append(self, update):
        self.updates.append(update)