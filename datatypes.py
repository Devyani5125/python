# 1.Write a program to building a simple student grade management system for a class of students. The system will store student names and their grades (both as lists) and should be able to perform the following operations:
# ●	Add a new student and their grade.
# ●	Update the grade of an existing student.
# ●	Remove a student from the list.
# ●	Calculate and display the average grade of the class.
# ●	Display the highest and lowest grades in the class.
# Tasks:
# ●	Use lists to store the student names and their corresponding grades.
# ●	Implement functions to add, update, remove, and calculate the average and extreme grades.
# Student Grade Management System

# # students = []
# # grades = []


# # def add_student():
# #     name = input("Enter student name: ")
# #     grade = float(input("Enter grade: "))

# #     students.append(name)
# #     grades.append(grade)

# #     print("Student added successfully.")


# # def update_grade():
# #     name = input("Enter student name to update: ")

# #     if name in students:
# #         index = students.index(name)
# #         new_grade = float(input("Enter new grade: "))
# #         grades[index] = new_grade

# #         print("Grade updated successfully.")
# #     else:
# #         print("Student not found.")


# # def remove_student():
# #     name = input("Enter student name to remove: ")

# #     if name in students:
# #         index = students.index(name)

# #         students.pop(index)
# #         grades.pop(index)

# #         print("Student removed successfully.")
# #     else:
# #         print("Student not found.")


# # def calculate_average():
# #     if len(grades) == 0:
# #         print("No student records available.")
# #     else:
# #         average = sum(grades) / len(grades)
# #         print("Average grade =", average)


# # def display_extreme_grades():
# #     if len(grades) == 0:
# #         print("No student records available.")
# #     else:
# #         highest = max(grades)
# #         lowest = min(grades)

# #         highest_index = grades.index(highest)
# #         lowest_index = grades.index(lowest)

# #         print("Highest grade =", highest,
# #               "obtained by", students[highest_index])

# #         print("Lowest grade =", lowest,
# #               "obtained by", students[lowest_index])


# # def display_students():
# #     if len(students) == 0:
# #         print("No student records available.")
# #     else:
# #         print("\nStudent Records")

# #         for i in range(len(students)):
# #             print(students[i], ":", grades[i])


# # while True:
# #     print("\nStudent Grade Management System")
# #     print("1. Add student")
# #     print("2. Update grade")
# #     print("3. Remove student")
# #     print("4. Calculate average grade")
# #     print("5. Display highest and lowest grades")
# #     print("6. Display all students")
# #     print("7. Exit")

# #     choice = int(input("Enter your choice: "))

# #     if choice == 1:
# #         add_student()

# #     elif choice == 2:
# #         update_grade()

# #     elif choice == 3:
# #         remove_student()

# #     elif choice == 4:
# #         calculate_average()

# #     elif choice == 5:
# #         display_extreme_grades()

# #     elif choice == 6:
# #         display_students()

# #     elif choice == 7:
# #         print("Program ended.")
# #         break

# #     else:
# #         print("Invalid choice.")

# # 2.# Function to calculate distance between two points
# def calculate_distance(point1, point2):
#     x1, y1 = point1
#     x2, y2 = point2

#     distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#     return distance


# # Function to find the farthest point from origin
# def farthest_from_origin(points):
#     farthest_point = points[0]
#     maximum_distance = calculate_distance((0, 0), points[0])

#     for point in points:
#         distance = calculate_distance((0, 0), point)

#         if distance > maximum_distance:
#             maximum_distance = distance
#             farthest_point = point

#     return farthest_point, maximum_distance


# Main program
# points = []

# n = int(input("Enter number of points: "))

# for i in range(n):
#     x = float(input("Enter x-coordinate: "))
#     y = float(input("Enter y-coordinate: "))

#     point = (x, y)
#     points.append(point)

# print("Points =", points)

# point1_number = int(input("Enter first point number: "))
# point2_number = int(input("Enter second point number: "))

# point1 = points[point1_number - 1]
# point2 = points[point2_number - 1]

# distance = calculate_distance(point1, point2)

# print("Distance between", point1, "and", point2, "=", distance)

# farthest_point, farthest_distance = farthest_from_origin(points)

# print("Farthest point from origin =", farthest_point)
# print("Distance from origin =", farthest_distance)
