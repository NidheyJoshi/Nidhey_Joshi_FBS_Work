# Program to calculate percentage of student based on 5 subjects

# Taking marks input for 5 subjects
marks = [5]
for i in range(1, 6):
    mark = float(input(f"Enter marks of subject {i}: "))
    marks.append(mark)

# Calculating total and percentage
total_marks = sum(marks)
percentage = (total_marks / (5 * 100)) * 100  # assuming each subject is out of 100

# Display results
print("\n--- Result ---")
print(f"Marks in 5 subjects: {marks}")
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
