firstSets = {'a', 'b', 'c', 1, 3} ## using {} for sets and the order can be different each time 
print(firstSets)

duplicateSets = {1, 1, 2, 3, 3, 'a'} ## unique value only
print(duplicateSets)

firstSets.add('d') ## adding an element to sets 
print(firstSets)

print('a' in firstSets) ## checking if it appears or not

firstSets.remove('c') ## removing an element from sets
print(firstSets)

print(len(firstSets)) ## print sets length

union = firstSets.union(duplicateSets) ## return a new set containing unique value from both set
print(union)

intersection = firstSets.intersection(duplicateSets) ## return a new set containing the same value from both sets
print(intersection)

difference = firstSets.difference(duplicateSets) ## return a new set that are in firstset but not in duplicateset
print(difference)

## This is tuple syntax
firstTuple = ('a', 'b', 'c') ## use () and cant be changed later
print(type(firstTuple))