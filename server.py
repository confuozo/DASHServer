#!/usr/bin/python

from flask import Flask, request, send_from_directory
import os
import json
import pprint
import datetime

app = Flask(__name__, static_folder='static')

def process(data):
    buffer_level = []
    for i in xrange(len(data[0].get('items', []))):
        try:
            time = datetime.datetime.strptime(data[0]['items'][i]['items'][0]['text'][3:], 
                "%a %b %d %Y %H:%M:%S %Z-0700 (PDT)").strftime('%Y-%m-%d %H:%M:%S')
            level = data[0]['items'][i]['items'][1]['text'][7:]
            buffer_level.append(time + ", " + level)
        except Exception as e:
            print e
    buffer_level_string = "\n".join(buffer_level)

    rep_switch = []
    for i in xrange(len(data[1].get('items', []))):
        try:
            time = datetime.datetime.strptime(data[0]['items'][i]['items'][0]['text'][3:], 
                "%a %b %d %Y %H:%M:%S %Z-0700 (PDT)").strftime('%Y-%m-%d %H:%M:%S')
            mt = data[1]['items'][i]['items'][1]['text'][4:]
            to = data[1]['items'][i]['items'][2]['text'][4:]
            rep_switch.append(time + ", " + mt + ", " + to)
        except Exception as e:
            print e
    rep_switch_string = "\n".join(rep_switch)

    return buffer_level_string, rep_switch_string


@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

@app.route('/sendvideometrics', methods=['GET', 'POST'])
def index():
    print request.form
    #pprint.pprint(json.loads(request.form['data']))
    bufferlevel, repswitch = process(json.loads(request.form['data']))
    #print data
    with open('vbufferlevel.txt', 'w') as f:
        f.write(bufferlevel);
    with open('vrep_switch.txt','w') as f:
        f.write(repswitch);
    return "Recorded"

@app.route('/sendaudiometrics', methods=['GET', 'POST'])
def audio():
    #print request.form
    # pprint.pprint(json.loads(request.form['data']))
    bufferlevel, repswitch = process(json.loads(request.form['data']))
    with open('abufferlevel.txt', 'w') as f:
        f.write(bufferlevel);
    with open('arep_switch.txt','w') as f:
        f.write(repswitch);
    return "Recorded"

    return "Recorded"

if __name__ == "__main__":
    app.run(debug = True)