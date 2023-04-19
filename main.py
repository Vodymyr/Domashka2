from flask import Flask, Response

app = Flask(__name__)


@app.route('/requirements')
def show_requirements():
    with open('requirements.txt', 'r') as file:
        requirements = file.read()
    return Response(requirements, mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True)
