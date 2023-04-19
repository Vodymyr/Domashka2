from flask import Flask, jsonify, request
from faker import Faker

app = Flask(__name__)
fake = Faker()

@app.route('/users/generate', methods=['GET'])
def generate_users():
    count = request.args.get('count', default=100, type=int)
    users = []

    for _ in range(count):
        user = {'name': fake.name(),'email': fake.email()}
        users.append(user)
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)