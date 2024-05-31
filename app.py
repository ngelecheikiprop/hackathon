from flask import Flask, request, redirect, url_for, render_template
import africastalking
import csv
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


class SMS:
    def __init__(self):
        self.username = "memyself"
        self.api_key = "535sdfdsa3336ccbf4ea3fa68asfdasfasdfsfddfd3837eabd3fadabdca1e185f4f"

        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self, file_path):
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                number_list = []
                number = line[3]
                number = f"+{number}"
                number_list.append(number)
                message = f"{line[0]} MARKS :\nENGLISH - {line[1]}\nKISWA - {line[2]}\n"
                try:
                    response = self.sms.send(message, number_list)
                    print(response)
                except Exception as e:
                    print('Encountered an error while sending: %s' % str(e))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        sms = SMS()
        sms.send(file_path)
        return 'File uploaded and SMS sent!'


if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
