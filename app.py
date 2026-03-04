from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the Flask App!")

@app.route('/health')
def health_check():
    return jsonify(status="healthy")

@app.route('/echo/<msg>')
def echo(msg):
    return jsonify(echo=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
