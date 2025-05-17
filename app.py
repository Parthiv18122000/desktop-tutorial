
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask-Mail configuration (for Gmail SMTP)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465  # For SSL
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your Gmail address
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your Gmail password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'  # Default sender

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inquiry', methods=['POST'])
def inquiry():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create the email message
        msg = Message(subject="New Inquiry from UniPilot",
                      recipients=["your-email@gmail.com"],  # Replace with your email
                      body=f"New inquiry received:\n\nName: {name}\nEmail: {email}\nMessage: {message}")

        # Send the email
        try:
            mail.send(msg)
            return render_template('thank_you.html', name=name)
        except Exception as e:
            return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
