import smtplib

to = input("Enter the Email of the recipient : \n")

content = input("Enter the content of the mail : \n")

# Turn on 2 step verification and generate App Password


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    sender = "sender@gmail.com"
    server.login(sender, "password")
    server.sendmail(sender, to, content)


sendEmail(to, content)
