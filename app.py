from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap5
import json 


app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    with open('projects.json') as f:
        projects_data = json.load(f)
    return render_template('index.html', projects=projects_data)

@app.route('/contact')
def contact():
    return render_template('contact_page.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)