from flask import Flask, render_template, url_for, jsonify
import subprocess

app = Flask(__name__)

@app.route('/run_python')
def run_python():
    try:
        subprocess.run(['python', 'C:/Users/du57/Desktop/Eduardo/Portfolio/eduSite/app.py'])
        return jsonify(success=True)
    except Exception as e:
        return jsonify(success=False, error=str(e))

