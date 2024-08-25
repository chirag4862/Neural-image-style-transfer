from flask import Flask, jsonify
from TransferImage import transfer

app = Flask(__name__)

@app.before_request
def before():
    print("This runs before anything!")

@app.route('/transfer/<string: content_path>/<string: style_path>/')
def transfer_image_data(content_path, style_path):
    return jsonify(transfer(content_path, style_path))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)