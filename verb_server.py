import json
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():

    with open("verbs.json", 'r') as fo:
        inputss = json.loads(fo.read())
        response = app.response_class(
            response=json.dumps(inputss),
            status=200,
            mimetype='application/json'
        )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


if __name__ == '__main__':
    app.run()
