from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': 'DevOps Demo Application',
        'status': 'running',
        'timestamp': datetime.datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
