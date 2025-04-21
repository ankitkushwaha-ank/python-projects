import requests
import smtplib
from email.mime.text import MIMEText
def get_location_and_send_email():
    try:

        response = requests.get('https://ipinfo.io')
        data = response.js()
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        loc = data.get('loc')

        #prepare the email content
        massage = f"location:{city},{region},{country}\nCoordinates:{loc}"

        #sending thr email
        sender_email = "ankitrajaryan247@gmail.com"
        recievers_email ="ankitrajank247@gmail.com"
        password = "8092345093@ankit"
        msg = MIMEText(massage)
        msg['subject'] = 'location info'
        msg['from'] = sender_email
        msg['to'] = recievers_email

    smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(sender_email,password)
        server.sendmail(sender_email,recievers_email,msg.as_string())

        print(f"location sent:{massage}")


get_location_and_send_email()



