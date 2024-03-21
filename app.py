from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        with open('test.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys())
            if csvfile.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
        return 'Data submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
