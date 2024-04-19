firstList = [1, 2, 4, 3] ## like an Array in JS
print(firstList[0])

firstList.append(5) ## adding an element to the end of list
print(firstList)

firstList.insert(5,6) ## insert 6 in index 5
print(firstList)

firstList.append(2)
firstList.remove(2) ## remove an element that matches the remove (first occurence)
print(firstList)

lastIndex = firstList.pop() ## remove the last element and show it 
print(lastIndex)
print(firstList)

del(firstList[0]) ## delete certain index from list
print(firstList)

print(len(firstList)) ## print a length of list
print(sorted(firstList)) ## sort a list (ordered)
reversed = firstList.reverse() ## just reverse tbe order but it doesnt return anything
print(firstList)

copyList = firstList.copy() ## copy the list so we dont modify the original one
copyList.append('Copy')
print(copyList)
print(firstList)
print(len(copyList)) ## print list's length


## list operator

double  = [2*item for item in firstList] ## like map in javascript
for item in double:
    print(item) ## print all the item with for loop

filteredList = [item for item in firstList if item < 5] ## like filter in javascript
print(filteredList)

