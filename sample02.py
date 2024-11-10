def main():
    # Prompt for file name
    filename = input("Enter file name: ")

    # Dictionary to store courses by department
    courses = {}

    # Try to open and read the file
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split(';')

                # Ensure line has exactly 3 parts
                if len(parts) != 3:
                    print("Error in file!")
                    return

                department, course_name, credit_points = parts[0], parts[1], parts[2]

                # Convert credit points to integer
                try:
                    credit_points = int(credit_points)
                except ValueError:
                    print("Error in file!")
                    return

                # Add course to the dictionary
                if department not in courses:
                    courses[department] = []
                courses[department].append((course_name, credit_points))

    except FileNotFoundError:
        print("Error opening file!")
        return

    # Command interface
    while True:
        print("\n[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit")
        command = input("Enter command: ").strip()
        command = command[0].lower() + command[1:]

        if command == 'p':
            print_all_courses(courses)
        elif command == 'r':
            department_name = input("Enter department name: ").strip()
            print_department_courses(courses, department_name)
        elif command == 'c':
            department_name = input("Enter department name: ").strip()
            print_department_credits(courses, department_name)
        elif command.startswith('a '):
            # Remove the initial 'a ' to pass the rest of the command to add_course
            user_input = command[2:].strip()  # This removes the "a " prefix
            add_course(courses, user_input)
        elif command.startswith('d'):
            #input("Enter deletion in format 'd <department>' or 'd <department> <course name>': ")
            # Remove the initial 'd ' to pass the rest of the command to add_course
            user_input = command[2:].strip()  # This removes the "d " prefix
            delete_course_or_department(courses, user_input)            
        elif command == 'q':
            print("Quitting the program.")
            break
        else:
            print("Invalid command!")
            print("\n[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit")            

def print_all_courses(courses):
    # Sort departments alphabetically
    for department in sorted(courses.keys()):
        print(f"*{department}")
        # Sort courses within each department alphabetically
        for course_name, credit_points in sorted(courses[department]):
            print(f"  {course_name} : {credit_points} cr")
def print_department_courses(courses, department_name):
    # Check if department exists
    if department_name not in courses:
        print("Department not found!")
        return

    # Print department courses in alphabetical order
    print(f"*{department_name}*")
    for course_name, credit_points in sorted(courses[department_name]):
        print(f"  {course_name} : {credit_points} cr")

def print_department_credits(courses, department_name):
    # Check if department exists
    if department_name not in courses:
        print("Department not found!")
        return

    # Calculate total credits for the department
    total_credits = sum(credit_points for _, credit_points in courses[department_name])
    print(f"Department {department_name} has to offer {total_credits} cr.")

def add_course(courses, user_input):
    # Find the last space in the input to separate credits
    try:
        *department_and_course, credit_points = user_input.rsplit(' ', 1)
        department_and_course = ' '.join(department_and_course)

        # Split remaining text to separate department from course name
        department, course_name = department_and_course.split(' ', 1)

        # Convert credit points to integer
        credit_points = int(credit_points)

    except ValueError:
        print("Invalid input format!")
        return

    # Add the course to the department
    if department not in courses:
        courses[department] = [(course_name, credit_points)]
        print(f"Added department {department} with course {course_name}")
    else:
        courses[department].append((course_name, credit_points))
        print(f"Added course {course_name} to department {department}")
# Append the new course to the file in the required format
    with open("courses.txt", "a") as file:
        file.write(f"{department};{course_name};{credit_points}\n")

def delete_course_or_department(courses, user_input):
    # Split the input into parts, expecting at least the department name
    parts = user_input.split(' ', 1)
    
    if len(parts) < 1:
        print("Invalid input format for delete command!")
        return

    department = parts[0]

    # Check if the department exists
    if department not in courses:
        print(f"Department {department} not found!")
        return

    if len(parts) == 1:
        # Delete the entire department
        del courses[department]
        print(f"Department {department} removed.")
    else:
        # Otherwise, try to delete the specific course within the department
        course_name = parts[1]  # This may be a multi-word course name
        for i, (name, _) in enumerate(courses[department]):
            if name == course_name:
                del courses[department][i]
                print(f"Department {department} course {course_name} removed.")
                
                # If no courses remain in the department, remove the department
                if not courses[department]:
                    del courses[department]
                break
        else:
            print(f"Course {course_name} from {department} not found!")
            return

    # Rewrite the file to reflect the deletion
    with open("courses.txt", "w") as file:
        for dept, courses_list in courses.items():
            for course, credits in courses_list:
                file.write(f"{dept};{course};{credits}\n")

    
if __name__ == "__main__":
    main()