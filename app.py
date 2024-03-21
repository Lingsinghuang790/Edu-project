from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST': #檢查客戶端發送的請求是否為 POST
        data = request.form.to_dict() #form.to_dict() 將表單資訊轉換為字典格式
        with open('test.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data.keys()) #將數據寫入CSV檔
            if csvfile.tell() == 0:  #檢查文件是否為空
                writer.writeheader() #將csv文件的標題行寫入文件
            writer.writerow(data) #將客戶端提交的數據寫入 csv 檔案
        #return'Data submitted successfully!'
    return redirect('/')

@app.route('/')
def render():
    return 


if __name__ == '__main__':
    app.run(debug=True)
