from flask import Flask, request
from pull import animalGroupMap

mappings = animalGroupMap()
app = Flask(__name__)


@app.route('/')
def helloWorld():
    return 'Hello World!'


@app.route('/animals', methods=['GET'])
def animals():
    singleAnimal = request.args.get('single', '')
    try:
        m = mappings.get(singleAnimal)
        return ','.join(m)
    except:
        return ''
