from flask import Flask, jsonify, request
import logging

from .password_generator import Generator

app = Flask(__name__)

generator = Generator()


@app.route('/')
def index():
    welcome_msg = (
        'This is passgen API. <br>'
        'Read the docs here: <br>'
        'https://github.com/varvara-krasavina/password_generator'
    )
    return welcome_msg


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
    chars = response.get('chars', None)

    if chars is None:
        password = generator.generate(passlen)
    else:
        password = generator.generate(passlen, chars=chars)

    return jsonify(
        {'response': password, 'passlen': passlen}
    ), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
