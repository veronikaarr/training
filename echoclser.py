#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#TASK
"""Напишите эхо клиент – сервер решение на базе flask где переданный клиентом json будет передан в виде xml назад."""

# EXAMPLE REQUEST
# curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"1"}' http://localhost:8080/login

# RESPONSE
# "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<userId>1</userId>"

#  IN THE FILE "EXREQ" ANOTHER EXAMPLE REQUEST


from flask import Flask
from flask import request
import json
import xmltodict

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    if not request.json:
        abort(400)
    jsonString = request.json
    xmltring = xmltodict.unparse(jsonString, pretty=True) #json to xml
    return json.dumps(xmltring)

if __name__ == '__main__':
    app.run(debug=True,port=8080)
