import smtplib

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Sender's credentials
sender_email = 'nirusan3.hariharan@gmail.com'
sender_password = 'IIT#123#123'

# Recipient's email
recipient_email = 'nirusan.hariharan350@gmail.com'

# Email content
subject = 'Patient Felt'
message = 'Hello, the patient has reported feeling unwell.'

try:
    # Create an SMTP object
    server = smtplib.SMTP(smtp_server, smtp_port)

    # Establish a secure connection
    server.starttls()

    # Login to the sender's email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, f'Subject: {subject}\n\n{message}')

    print('Email sent successfully!')

except smtplib.SMTPAuthenticationError:
    print('Authentication error. Please check your username and password.')

except smtplib.SMTPException as e:
    print(f'An error occurred while sending the email: {str(e)}')

finally:
    # Close the connection to the SMTP server
    server.quit()
