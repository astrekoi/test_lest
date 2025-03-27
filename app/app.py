from flask import jsonify
from app_factory import create_app

app = create_app()

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/count')
def count():
    try:
        count = app.redis.incr('counter')
        return jsonify({"count": count})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)