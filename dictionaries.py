firstDictionaries = {
    1 : "satu",
    2 : "dua",
    3 : "tiga"
} ## dictionaries like JSON 

print(firstDictionaries)
print(firstDictionaries[1]) ## print certain values based on keys

print(firstDictionaries.keys()) ## print only keys
print(firstDictionaries.values()) ## print only values

for item in firstDictionaries:
    print(item)