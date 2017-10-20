from flask import Flask, request, render_template
from pull import animalGroupMap

mappings = animalGroupMap()
app = Flask(__name__)


@app.route('/')
def helloWorld():
    return render_template('index.html')


@app.route('/collective', methods=['GET'])
def collective():
    subject = request.args.get('subject', '')
    try:
        m = mappings.get(subject)
        return ','.join(m)
    except:
        return ''
