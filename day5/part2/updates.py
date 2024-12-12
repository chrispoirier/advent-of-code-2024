from typing import List
from rules import rules

class update:
    def __init__(self, line):
        self.pages: List[int] = []
        self.valid: bool = None
        for page in line.split(','):
            self.pages.append(int(page))

    def is_valid(self, rulesObj: rules):
        if self.valid is not None:
            return self.valid
        
        myRules = rulesObj.get_rules_by_all(self.pages)
        #print([r.string() for r in myRules.rules])
        return myRules.validate(self.pages)
    
    def fix(self, rulesObj: rules):
        myRules = rulesObj.get_rules_by_all(self.pages)
        #print([r.string() for r in myRules.rules])
        while not self.is_valid(rulesObj):
            for r in myRules.rules:
                if not r.validate(self.pages):
                    temp = self.pages[self.pages.index(r.first)]
                    self.pages[self.pages.index(r.first)] = self.pages[self.pages.index(r.second)]
                    self.pages[self.pages.index(r.second)] = temp
            self.valid = None

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

    def get_invalid_updates(self, rulesObj: rules):
        invalidUpdates = updates([])
        for u in self.updates:
            #print(u.pages)
            if not u.is_valid(rulesObj):
                #print("invalid")
                invalidUpdates.append(u)
                #print([u.pages for u in invalidUpdates.updates])
            #else:
                #print("valid")
            #print("----")
        return invalidUpdates
    
    def append(self, update):
        self.updates.append(update)