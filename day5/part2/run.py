import sys
sys.path.append('../../')
from common.fileio import read_input
from rules import rules
from updates import updates
import math

# data = read_input("test.txt")
data = read_input("input.txt")

rulesStr = data[:data.index('')]
rulesObj = rules(rulesStr)

updatesStr = data[data.index('') + 1:]
updatesObj = updates(updatesStr)

invalidUpdates = updatesObj.get_invalid_updates(rulesObj)
middleSum = 0
for u in invalidUpdates.updates:
    # print(u.pages)
    u.fix(rulesObj)
    # print(u.pages)
    middlePage = u.pages[math.ceil(len(u.pages) / 2) - 1]
    #print(middlePage)
    middleSum += middlePage

print(middleSum)