import smtplib
from email.message import EmailMessage

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp: #this would be custom to whatever email service you are using.
    smtp.ehlo()         #this is the initial 'handshake'
    smtp.starttls()     #encryption method - connecting securily 
    smtp.ehlo()         #another handshake 
    smtp.login('devon.fullstack.dev@gmail.com', 'uxvhvmhgichdalqr')
    subject = 'Hello there - sent from my IDE hehe'
    body = "Hello agian \nI am sending this from my IDE - I really hope this F****** works :) \nBest regards and warmest welcome\nyah boi\nDrizzy"
    msg = f'subject:{subject} \n\n{body}'
    smtp.sendmail('devon.fullstack.dev@gmail.com', 'devon.fullstack.dev@gmail.com', msg)
    print('the email has been sent')



#random note - if you call your script 'email.py' this could result in an error
