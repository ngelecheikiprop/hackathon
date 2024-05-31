import csv


def main():
    # Load data
    with open('students_results.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(reader)
        for row in reader:
            name = row['name']
            english_marks = row['english']
            kiswahili_marks = row['kiswahili']
            parent_number = row['parent_number']

            # Format the message
            message = f"Dear Parent, your child {name} has scored {english_marks} in English and {kiswahili_marks} in Kiswahili."

            # Print the message
            print(f"Message to {parent_number}: {message}")


if __name__ == "__main__":
    main()