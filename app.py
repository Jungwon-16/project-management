from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbpjt


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/new', methods=['POST'])
def pjt_list():
    title = request.form['title']
    start = request.form['start']
    end = request.form['end']
    task = request.form['task']
    member = request.form['member']

    pjt = {
        'title': title,
        'start': start,
        'end': end,
        'task': task,
        'member': member
    }

    db.pjts.insert_one(pjt)
    return jsonify({'result': 'success', 'msg': '프로젝트 등록 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)