import sys
from pubService import PubService
from subService import SubService
from producerAPI import kafkaProducer
from consumerAPI import kafkaconsumer

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'publisher':
            if request.form['pass'] == 'pppp':
                print('correct password!', file=sys.stderr)
                return redirect('/publishers')
            else:
                m = "Wrong Password"
                return render_template('index.html', msg=m)
                print('wrong password!', file=sys.stderr)
        elif request.form['submit_button'] == 'subscriber':
            if request.form['pass'] == 'ssss':
                print('correct password!', file=sys.stderr)
                return redirect('/subscribers')
            else:
                m = "Wrong Password"
                return render_template('index.html', msg=m)
                print('wrong password!', file=sys.stderr)
    return render_template('index.html')


@app.route('/publishers', methods=['GET', 'POST'])
def frompublishers():
    if request.method == 'POST':
        pid = request.form['publisherid']
        eid = int(request.form['dropdown'])
        if request.form['submit'] == 'advertise':
            PubService.advertise(pid, eid)
        elif request.form['submit'] == 'deadvertise':
            PubService.deadvertise(pid, eid)
        elif request.form['submit'] == 'publish':
            kafkaProducer(eid)
            m = PubService.viewAd(pid, eid)
            return render_template('index.html', msg=m)
    return render_template('pub.html')


@app.route('/subscribers', methods=['GET', 'POST'])
def fromsubscribers():
    if request.method == 'POST':
        sid = request.form['subscriberid']
        eid = int(request.form['dropdown'])
        if request.form['submit'] == 'subscribe':
            SubService.subscribe(sid, eid)
        elif request.form['submit'] == 'unsubscribe':
            SubService.unsubscribe(sid, eid)
        elif request.form['submit'] == 'updates':
            updates = kafkaconsumer(eid)
            return render_template('sub.html', u=updates)
    return render_template('sub.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
