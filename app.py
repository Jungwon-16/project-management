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
    pjt_title = request.form['pjt_title']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    m_task = request.form.getlist('m_task[]')
    m_member = request.form.getlist('m_member[]')

    pjt = {
        'pjt_title': pjt_title,
        'start_date': start_date,
        'end_date': end_date,
        'm_task': m_task,
        'm_member': m_member
    }

    db.pjts.insert_one(pjt)
    return jsonify({'result': 'success', 'msg': '프로젝트 등록 완료!'})


@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/detail', methods=['POST'])
def s_pjt_list():
    pjt_title = request.form['pjt_title']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    s_task_list = request.form.getlist('s_task_list[]')
    pjt_memo = request.form.getlist('pjt_memo')

    s_pjt = {
        'pjt_title': pjt_title,
        'start_date': start_date,
        'end_date': end_date,
        's_task_list': s_task_list,
        'pjt_memo': pjt_memo
    }

    db.pjts.insert_one(s_pjt)
    return jsonify({'result': 'success', 'msg': '프로젝트 등록 완료!'})


@app.route('/reg_pjt', methods=['GET'])
def d_pjt_list():
    pjts = list(db.pjts.find({},{'_id':0}))
    return jsonify({'result': 'success', 'pjts': pjts})

@app.route('/status')
def status():
    return render_template('status.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)