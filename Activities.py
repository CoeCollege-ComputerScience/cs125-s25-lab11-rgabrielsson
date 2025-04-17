#0
set1 = set("abcdijklm")
set2 = set("dijnopefgh")
set3 = set("klmijnopqrst")

print(set1.intersection(set2,set3))
print(set1.difference(set2,set3))
print(set2.intersection(set3))
print((set1.intersection(set2)).difference(set3))
print((set1.symmetric_difference(set2)).intersection(set3))





#1
def majors():
    infile1 = open("cs.txt", "r")
    infile1.readline()  
    csMajors = set()
    for line in infile1:
        line = line.strip()
        csMajors.add(line)

    infile2 = open("math.txt", "r")
