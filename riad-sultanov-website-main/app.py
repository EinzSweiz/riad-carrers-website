from flask import Flask, json, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        "id":1,
        "title": "Data Analyst",
        "location": "Baku, Azerbaijan",
        "salary": "1000$"
    },
    {
        "id":2,
        "title": "Frontend Developer",
        "location": "Baku, Azerbaijan",
        "salary": "1500$"
    },
    {
        "id":3,
        "title": "Backend Developer",
        "location": "NewYork, USA",
        "salary": "2000$"
    }
]
@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)
@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)