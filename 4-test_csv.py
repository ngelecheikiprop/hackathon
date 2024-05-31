import csv

with open('students_results.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        number = line[3]
        number = f"+{number}"
        print(f"the number is: {number}")
        message = f"{line[0]} MARKS :\nENGLISH - {line[1]}\nKISWA - {line[2]}"
        print(f"{message}")
        print("--------------")
