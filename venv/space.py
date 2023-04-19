import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def heloo_world():
    return "Hello Flask"
@app.route('/space/', methods=['GET'])
def get_astronauts():
    try:
        url = 'http://api.open-notify.org/astros.json'
        response = requests.get(url)
        data = response.json()

        number_of_astronauts = data['number']

        result = {'number_of_astronauts': number_of_astronauts}
        return jsonify(result)

    except Exception as e:
        return f'Сталася помилка: {e}'

if __name__ == '__main__':
    app.run(debug=True)