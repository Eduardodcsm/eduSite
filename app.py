# app.py

from flask import Flask, render_template
from subprocess import run

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_python_program')
def new_python_program():
    # Include the logic to execute your GUIbox.py here
    # For simplicity, let's just return a message
    return "Executing GUIbox.py"

@app.route('/execute_gui_box')
def execute_gui_box():
    run(["python", "GUIbox.py"])
    return "Executing GUIbox.py"

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
