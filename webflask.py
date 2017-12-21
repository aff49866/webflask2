from flask import Flask
from flask import render_template
from flask import url_for
import os
from config import APP_STATIC_TXT
app = Flask(__name__)

@app.route('/')
def table():
    domainlist = []
    file = os.path.dirname(os.path.abspath(__file__)) + r'\static\jingjia.txt'
    print(os.path.dirname(os.path.abspath(__file__)) + r'\static\jingjia.txt')
    with open(file) as f:
        for domain in f.readlines():
            domainlist.append(domain.rstrip('\n'))
    data = domainlist
    return render_template('table.html',data=data)

if __name__ == '__main__':
    app.run()
