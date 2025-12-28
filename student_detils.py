# Student Grade Calculator

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"

def main():
    # Accept student details
    name = input("Enter student name: ")
    department = input("Enter department: ")
    semester = input("Enter semester: ")

    # Accept marks in three subjects
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    # Calculate average
    avg = sum(marks) / 3

    # Determine grade
    grade = calculate_grade(avg)

    # Display student details and grade
    print("\n--- Student Report ---")
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Semester   : {semester}")
    print(f"Marks      : {marks}")
    print(f"Average    : {avg:.2f}")
    print(f"Grade      : {grade}")

if __name__ == "__main__":
    main()
