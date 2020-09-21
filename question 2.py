#Question 2

"""
Write a program that calculates the average score on an exam. Assume we have a small class of only three
students. Assign each student’s score to variables called student1, student2, and student3 and then use
these variables to find the average score. Assign the average to a variable called average. Print the student
scores and the average score.
The following demonstrates the program output when the students have been assigned scores
of 80.0, 90.0, and 66.5:
Student scores:
80.0
90.0
66.5
Average: 78.83333333333333
"""
print("Student scores:")
student1 = input()
student2 = input()
student3 = input()
average = (float(student1) + float(student2) + float(student3))/3.0
print("Average:", average)