# student_grade.py
# Program to calculate student grade
import sys

def calculate_grade(avg):
    """Return grade based on average marks."""
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    print("=== Student Grade Calculator ===")

    try:
        if len(sys.argv) == 7:
            # Case 1: Arguments passed (CLI / Jenkins)
            name = sys.argv[1]
            dept = sys.argv[2]
            sem = sys.argv[3]
            m1 = float(sys.argv[4])
            m2 = float(sys.argv[5])
            m3 = float(sys.argv[6])
        else:
            # Case 2: Console input
            name = input("Enter Student Name: ")
            dept = input("Enter Department: ")
            sem = input("Enter Semester: ")
            m1 = float(input("Enter Marks in Subject 1: "))
            m2 = float(input("Enter Marks in Subject 2: "))
            m3 = float(input("Enter Marks in Subject 3: "))

        avg = (m1 + m2 + m3) / 3
        grade = calculate_grade(avg)

        print("\n=== Student Details ===")
        print("Name:", name)
        print("Department:", dept)
        print("Semester:", sem)
        print("Average Marks:", round(avg, 2))
        print("Grade:", grade)

    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")
