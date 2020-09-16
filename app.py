from flask import Flask, jsonify, request
import logging

from password_generator import gen_password

app = Flask(__name__)

@app.route('/passgen/api/v1.0/', methods=['GET'])
def generate():
    response = request.json

    if not response or 'passlen' not in response:
        error_msg = "Missing required argument 'passlen'."
        logging.error(error_msg)
        return jsonify(
            {
                'response': None,
                'passlen': None,
                'error': error_msg
            }
        ), 200

    passlen = response['passlen']

    if 'chars' in response:
        chars = response['chars']
        password = gen_password(passlen, chars=chars)
    else:
        password = gen_password(passlen)

    return jsonify(
        {'response': password, 'passlen': passlen}
    ), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
