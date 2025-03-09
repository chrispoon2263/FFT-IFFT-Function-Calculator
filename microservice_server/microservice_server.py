from flask import Flask, jsonify
import random

app = Flask(__name__)



@app.route('/', methods=['GET'])
def home():
    random_functions = ["x^2", "x^3", "1 + 2x", "x^5", "x + 1"]
    print("")
    print("********************************************")
    print("Listening... for randomize click")
    print("")
    print("Received message and generating 2 random functions for you!")
    print("Calculating...")
    print("")
    input_1 = random.choice(random_functions)
    input_2 = random.choice(random_functions)
    print("Sending...")
    print("Sending input 1: " + str(input_1))
    print("Sending input 2: " + str(input_2))

    print("********************************************")
    return jsonify({"input_1": input_1, "input_2": input_2})


if __name__ == '__main__':
    app.run(host='localhost', port=65398)
