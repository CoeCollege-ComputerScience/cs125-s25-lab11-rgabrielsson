#0
def sets():
    set1 = set("abcdijklm")
    set2 = set("dijnopefgh")
    set3 = set("klmijnopqrst")

    print(set1.intersection(set2,set3))
    print(set1.difference(set2,set3))
    print(set2.intersection(set3))
    print((set1.intersection(set2)).difference(set3))
    print((set1.symmetric_difference(set2)).intersection(set3))

sets()



#1
def getSet(filename):
    infile = open(filename, "r")
    infile.readline()  
    set1 = set()
    for line in infile:
        line = line.strip()
        set1.add(line)
    infile.close()
    return set1

def print_to_file(filename, set,message):
    outfile = open(filename,"a")
    print(message, file = outfile)
    for item in set:
        print(item, file = outfile)
    outfile.close

def majors():
    csMajors = getSet("cs.txt")
    mathMajors = getSet("math.txt")
    students = getSet("studentYear.txt")
    freshman = set()
    sophomore = set()
    junior = set()
    senior = set()
    for line in students:
        year = line[0]
        if year == "1":
            freshman.add(line[1:].strip())
        elif year == "2":
            sophomore.add(line[1:].strip())
        elif year == "3":
            junior.add(line[1:].strip())
        else:
            senior.add(line[1:].strip())

    #clears file each time
    outfile = open("StudentInfo.txt","w")
    outfile.close

    print_to_file("StudentInfo.txt",csMajors.intersection(mathMajors),"CS-Math double majors:")
    print_to_file("StudentInfo.txt",csMajors.union(mathMajors),"Math or CS majors:")
    print_to_file("StudentInfo.txt",csMajors.difference(mathMajors),"CS majors not in Math:")
    

    print_to_file("StudentInfo.txt",sophomore.union(csMajors),"Sophomore CS majors:")
    print_to_file("StudentInfo.txt",freshman.difference(csMajors,mathMajors),"Non-math and non-CS freshman:")

    #interpreted to mean any senior majoring in both math and CS (double majors)
    print_to_file("StudentInfo.txt",senior.intersection(mathMajors,csMajors),"Senior math and CS majors:")

majors()