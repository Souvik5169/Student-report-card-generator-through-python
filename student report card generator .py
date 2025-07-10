import csv
import os

FILE_NAME = "student_records.csv"

def calculate_grade(percent):
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B+"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C"
    else:
        return "Fail"

def create_file_if_not_exists():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Roll", "Class", "Subjects", "Marks", "Total", "Percentage", "Grade"])

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    student_class = input("Enter class: ")

    subjects = []
    marks = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        subject = input(f"Enter subject {i+1} name: ")
        mark = float(input(f"Enter marks for {subject} (out of 100): "))
        subjects.append(subject)
        marks.append(mark)

    total = sum(marks)
    percent = (total / (n * 100)) * 100
    grade = calculate_grade(percent)

    with open(FILE_NAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            name,
            roll,
            student_class,
            "|".join(subjects),
            "|".join(str(m) for m in marks),
            total,
            percent,
            grade
        ])
    
    print(f"\n✅ Student {name}'s data saved successfully!\n")

def show_all_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("-" * 40)
            print(f"Name      : {row['Name']}")
            print(f"Roll No   : {row['Roll']}")
            print(f"Class     : {row['Class']}")
            subjects = row["Subjects"].split("|")
            marks = row["Marks"].split("|")
            for sub, mark in zip(subjects, marks):
                print(f"{sub:<12}: {mark}/100")
            print(f"Total     : {row['Total']}")
            print(f"Percentage: {row['Percentage']}%")
            print(f"Grade     : {row['Grade']}")
            print("-" * 40 + "\n")

def search_student():
    roll = input("Enter roll number to search: ")
    found = False
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Roll"] == roll:
                found = True
                print("\nStudent Found:")
                print(f"Name      : {row['Name']}")
                print(f"Roll No   : {row['Roll']}")
                print(f"Class     : {row['Class']}")
                subjects = row["Subjects"].split("|")
                marks = row["Marks"].split("|")
                for sub, mark in zip(subjects, marks):
                    print(f"{sub:<12}: {mark}/100")
                print(f"Total     : {row['Total']}")
                print(f"Percentage: {row['Percentage']}%")
                print(f"Grade     : {row['Grade']}")
                break
    if not found:
        print("❌ Student not found.")

def class_analysis():
    class_name = input("Enter class to analyze: ")
    total_students = 0
    total_percent = 0
    topper = {"name": "", "percent": 0}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Class"] == class_name:
                percent = float(row["Percentage"])
                total_percent += percent
                total_students += 1
                if percent > topper["percent"]:
                    topper["name"] = row["Name"]
                    topper["percent"] = percent

    if total_students == 0:
        print("No data found for this class.")
    else:
        avg_percent = total_percent / total_students
        print(f"\n📊 Class {class_name} Analysis:")
        print(f"Total Students : {total_students}")
        print(f"Average %      : {avg_percent:.2f}%")
        print(f"Topper         : {topper['name']} with {topper['percent']}%")

def main_menu():
    create_file_if_not_exists()
    while True:
        print("\n🎓 Student Report Card System")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll No.")
        print("4. Class Analytics")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_analysis()
        elif choice == "5":
            print("Exiting... Have a great day! 👋")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()