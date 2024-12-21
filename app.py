from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

data = [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]

@app.route("/")
def func():
    return "Hello World"

@app.route("/api", methods=['GET'])
def api():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0' , port=5003)


#  gunicorn --bind 0.0.0.0:8001 app:app