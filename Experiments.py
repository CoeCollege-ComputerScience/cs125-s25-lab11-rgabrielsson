#1

set1 = set("abcdefg")
print(set1)
set2 = set("adejgisnif")
print(set2)
set3 = set("aaaaaaaaa")
print(set3)

#2

#sets are mutable
set1.remove("a")
print(set1)

#sets are not ordered or indexable
#print(set2[0])

#sets are iterable
for i in set2:
    print(i)

#you can determine the length of a set
print(len(set1))

#you can check if an element is in a set
print("e" in set1)


#4
set4 = set("abcdefg")
set4.add("h")
print(set4)
set4.remove("a")
print(set4)
set4.pop()             #removes a random element
print(set4)
# set4.pop("c")
# print(set4)


#5
print("-"*30)

set1 = set("abcdefg")
print(set1)
set2 = set("adegjke")
print(set2)
set3 = set("aaaaaaaaa")
print(set3)

set1.intersection(set2)           #does not change set1
print(set1)
print("-"*30)
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))

set4 = set1.symmetric_difference(set2)
print(set4.isdisjoint(set1))
print(set4.isdisjoint(set2))
print(set4.isdisjoint(set3))

