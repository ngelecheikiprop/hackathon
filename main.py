"""
mzazidigital software as a service
"""
from __future__ import print_function
import africastalking
import csv

"""
name,english,kiswahili,parent_number
"""


class SMS:
    def __init__(self):
        self.username = "ngelechei"
        self.api_key = "53536ccbf4ea3adfdsfdsafas1242342617e3837eabd3fadabdca1e185f4f"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # ---------------------------------
        with open('students_results.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                number_list = []
                number = line[3]
                number = f"+{number}"
                number_list.append(number)
                message = f"{line[0]} MARKS :\nENGLISH - {line[1]}\nKISWA - {line[2]}\n"
                try:
                    # Thats it, hit send and we'll take care of the rest.
                    response = self.sms.send(message, number_list)
                    print(response)
                except Exception as e:
                    print('Encountered an error while sending: %s' % str(e))

        # ---------------------------------------
if __name__ == '__main__':
    SMS().send()
