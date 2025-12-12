from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap5
import json 
from forms import ContactForm
import email_validator
from flask import redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = '0380YGFANVJVPASDFKJH3498YVSDKJFHSDF'
bootstrap = Bootstrap5(app)

@app.route('/')
def home():
    with open('projects.json') as f:
        projects_data = json.load(f)
    return render_template('index.html', projects=projects_data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        print(f"Name: {form.name.data}, Email: {form.email.data}")
        return redirect(url_for('home'))
        # Here you would typically handle the form submission,


    return render_template('contact_page.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5001)