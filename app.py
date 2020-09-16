from flask import Flask, jsonify, request

from password_generator import gen_password

app = Flask(__name__)

@app.route('/passgen/api/v1.0/', methods=['GET'])
def generate():
    response = request.json

    passlen = response['passlen']
    password = gen_password(passlen)

    return jsonify(
        {'response': password, 'passlen': passlen}
    ), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
