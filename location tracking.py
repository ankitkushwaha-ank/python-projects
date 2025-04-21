import requests
import smtplib
from email.mime.text import MIMEText


def get_location_and_send_email():
    try:
        # Get location details
        response = requests.get('https://ipinfo.io')
        data = response.json()

        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        loc = data.get('loc')

        # Prepare the email content
        message = f"Location: {city}, {region}, {country}\nCoordinates: {loc}"

        # Sending the email (example with Gmail)
        sender_email = "ankitrajaryan247@gmail.com"
        receiver_email = "ankitrajank247@gmail.com"  # Set this to your email address
        password = "8092345093@ankit"  # Use an app-specific password if necessary

        msg = MIMEText(message)
        msg['Subject'] = 'Location Info'
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Establish connection to the email server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        print(f"Location sent: {message}")

    except Exception as e:
        print(f"Error: {e}")


# if _name_ == "_main_":
    get_location_and_send_email()