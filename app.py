from flask import Flask, jsonify, render_template
from flask_bootstrap import Bootstrap5
import json 
from forms import ContactForm
import email_validator
from flask import redirect, url_for
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = os.getenv('GMAIL_SENDER_ADDRESS')
smtp_password = os.getenv('GMAIL_PASSWORD')
smtp_recipient = os.getenv('GMAIL_RECEIPIENT_ADDRESS')



app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
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
        
        #send me email with details
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, smtp_recipient, message=f"Subject: Contact Form Submission\n\nName: {form.name.data}\nEmail: {form.email.data}\nMessage: {form.message.data}")
            print("Email sent successfully!")

        return redirect(url_for('home'))
        # Here you would typically handle the form submission



    return render_template('contact_page.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=5001)