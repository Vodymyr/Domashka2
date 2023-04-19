import csv
from statistics import mean
from faker import Faker
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/mean/', methods=['GET'])
def calculate_mean():
    file_path = 'hw.csv'
    heights = []
    weights = []

    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                height = float(row[0])
                weight = float(row[1])
                heights.append(height)
                weights.append(weight)

        fake = Faker()
        for _ in range(100):
            height = fake.uniform(150, 200)
            weight = fake.uniform(50, 100)
            heights.append(height)
            weights.append(weight)

        mean_height = mean(heights)
        mean_weight = mean(weights)

        result = {'mean_height': mean_height, 'mean_weight': mean_weight}
        return jsonify(result)

    except Exception as e:
        return f'Сталася помилка: {e}'

if __name__ == '__main__':
    app.run(debug=True)
print(42)