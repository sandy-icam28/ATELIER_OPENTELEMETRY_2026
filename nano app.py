#!/usr/bin/env python3
from flask import Flask, jsonify
import time, random

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello OTel from Flask!"

@app.route("/work")
def work():
    time.sleep(random.uniform(0.05, 0.25))
    return jsonify(status="ok")

@app.route("/error")
def boom():
    raise RuntimeError("boom")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
