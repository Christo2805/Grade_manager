students = []  


def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    name = input("Name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    try:
        mark = int(input("Mark (0-100): "))
    except ValueError:
        print("Please enter a number.")
        return
    if mark < 0 or mark > 100:
        print("Mark must be between 0 and 100.")
        return
    students.append([name, mark])
    print("Added!")


def show_results():
    if len(students) == 0:
        print("No students yet.")
        return
    print(f"{'Name':<12}{'Mark':>5}{'Grade':>7}")
    marks = []
    for name, mark in students:
        print(f"{name:<12}{mark:>5}{get_grade(mark):>7}")
        marks.append(mark)
    average = sum(marks) / len(marks)
    print(f"Average: {average:.1f}  Highest: {max(marks)}  Lowest: {min(marks)}")


while True:
    print("\n1. Add  2. Show  3. Quit")
    choice = input("Choose: ").strip()
    if choice == "1":
        add_student()
    elif choice == "2":
        show_results()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

