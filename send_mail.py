import smtplib
from email.mime.text import MIMEText

def send_mail(customer, employee, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = ''
    password = ''
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer} </li><li>Employee: {employee} </li><li>Rating: {rating} </li><li>Comments: {comments} </li></ul>"

    sender_email = 'email@mail.com'
    receiver_email = 'email@mail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'ECF Employee Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP(smtp_server,port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())