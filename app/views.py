# This route serves the dictionary d at the route /api/data
import datetime
from flask import jsonify, render_template
from flask import send_from_directory

import json 
from app import app 
from app import hw_views
from flask import (jsonify, render_template,
                   request, url_for, flash, redirect)

@app.route("/")
def home():
    return "Flask says 'Hello world!'"


@app.route('/crash')
def crash():
    return 1/0


@app.route('/lab03')
def lab03_home():
    return render_template('lab03/index.html',
                           utc_dt=datetime.datetime.utcnow())

@app.route('/lab03/about/')
def lab03_about():
    return render_template('lab03/about.html')

@app.route('/lab03/comments/')
def lab03_comments():
    raw_json = read_file('app/data/messages.json')
    messages = json.loads(raw_json)
    return render_template('lab03/comments.html', comments=messages)





@app.route('/lab04')
def lab04_bootstrap():
    return send_from_directory('static','lab04_bootstrap.html')



def read_file(filename, mode="rt"):
    with open(filename, mode, encoding='utf-8') as fin:
        return fin.read()


def write_file(filename, contents, mode="wt"):
    with open(filename, mode, encoding="utf-8") as fout:
        fout.write(contents)


@app.route('/lab03/create/', methods=('GET', 'POST'))
def lab03_create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']


        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            raw_json = read_file('app/data/messages.json')
            messages = json.loads(raw_json)
            messages.append({'title': title, 'content': content})
            write_file('app/data/messages.json',
                       json.dumps(messages, indent=4))
            return redirect(url_for('lab03_comments'))


    return render_template('lab03/create.html')