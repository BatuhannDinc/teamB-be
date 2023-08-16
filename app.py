from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS desteğini ekleyin

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operator = data['operator']
    num1 = data['num1']
    num2 = data['num2']

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operator'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
