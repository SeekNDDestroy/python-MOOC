noOfStudents = int(input("How many students on the course?"))
groupSize = int(input("Desired group size?"))

noOfGroups = noOfStudents // groupSize
if noOfStudents % groupSize != 0:
    noOfGroups += 1
    print("Number of groups formed:",noOfGroups)
else:
    print("Number of groups formed:",noOfGroups)
