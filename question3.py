#Question 3

"""
 Imagine that you teach three classes. These classes have 32, 45, and 51 students. You want to divide the
students in these classes into groups with the same number of students in each group, but you recognize
that there may be some “left over” students. Assume that you would like there to be 5 groups in the first
class (of 32 students), 7 groups in the second class (of 45 students), and 6 groups in the third class (of 51
students). Write a program to calculate the number of students in each group (where each group has the
same number of students). Print this number for each class and also print the number of students that will
be “leftover” (i.e., the number of students short of a full group). Use
simultaneous assignment to assign the number in each group and the “leftover” to variables.
The following demonstrates the program’s output:
Number of students in each group:
Class 1: 6
Class 2: 6
Class 3: 8
Number of students leftover:
Class 1: 2
Class 2: 3
Class 3: 3
"""
#number of students in each class
class1 = 32
class2 = 45
class3 = 51

#number of groups in each class
group_number1 = 5
group_number2 = 7
group_number3 = 6

#number of students in each class
group_class1, group_class2, group_class3 = class1//group_number1, class2//group_number2, class3//group_number3

#number of leftovers
leftovers1, leftovers2, leftovers3 = class1%group_number1, class2%group_number2, class3%group_number3

print("Number of students in each group:")
print("Class 1:", str(group_class1))
print("Class 2:", str(group_class2))
print("Class 3:", str(group_class3))

print("\n")

print("Number of students leftover:")
print("Class 1:", str(leftovers1))
print("Class 2:", str(leftovers2))
print("Class 3:", str(leftovers3))