from flask import Flask, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    # Get current timestamp in ISO format
    timestamp = datetime.utcnow().isoformat()
    # Get visitor's IP (handle X-Forwarded-For for load balancers)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return {
        "timestamp": timestamp,
        "ip": ip
    }

if __name__ == '__main__':
    # Bind to 0.0.0.0 for Docker; use port from environment or default to 8080
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)