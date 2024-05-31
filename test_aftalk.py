# works with both python 2 and 3
from __future__ import print_function

import africastalking


class SMS:
    def __init__(self):
        self.username = "memyself"
        self.api_key = "53536ccbf4ea3fa689f65dkdjskjdkjskd837eabd3fadabdca1e1asfdsff"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        recipients = ["+254700000000"]

        # Set your message
        message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"

        # message = f"END TERM RESULTS OF  {student_name}\nENGLISH : {english_results}\n kiswa:{kiswa_results}"

        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
    SMS().send()

    # csv    name | english | kiswa | parent number    sumarry of x results
    """
    END TERM RESULTS
    sumarry of x results:
    English : 50
    kiswa : 50 
    """
