from flask import Flask, request, jsonify
import json

app = Flask(__number__)

@app.route('/calculation', methods=['GET'])
def calculation_path():
    number = request.args.get('number', 10)
    number_real = int(number)
    number_analyzed = number_real * number_real
    output = json.dumps({
        "entered_number" : number_real,
        "number_squared" : number_analyzed
    })
    return output
