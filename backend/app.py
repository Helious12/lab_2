from flask import Flask
import random
import os
app = Flask(__name__)
port = os.getenv("PORT", 5001)
@app.route("/")
def home():
    return f"Backend on port {port}"
@app.route("/data")
def data():
    return {"value": random.randint(1, 100)}
@app.route("/status")
def status():
    return {"service": "backend", "port": port}
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)