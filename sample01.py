def main():
    # Prompt for file name
    filename = input("Enter file name: ")
    
    try:
        # Try to open the file
        with open(filename, 'r') as file:
            for line in file:
                # Strip any trailing whitespace
                line = line.strip()
                
                # Split line into parts by semicolon
                parts = line.split(';')
                
                # Check if there are exactly three parts
                if len(parts) != 3:
                    print("Error in file!")
                    return
                
                # Try to parse the credit points as an integer
                try:
                    department = parts[0]
                    course_name = parts[1]
                    credit_points = int(parts[2])
                    
                    # You can add more processing here if needed
                    print(f"Department: {department}, Course: {course_name}, Credits: {credit_points}")
                
                except ValueError:
                    print("Error in file!")
                    return

    except FileNotFoundError:
        # If file cannot be opened
        print("Error opening file!")
        return

# Run the main function
if __name__ == "__main__":
    main()
