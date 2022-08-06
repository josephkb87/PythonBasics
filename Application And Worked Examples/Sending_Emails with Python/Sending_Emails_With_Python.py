# We create a python program that shows how to send Email(s) in Python


import smtplib  # This imports the smtp server lib for email comm

def send_email(host, subject, to_addr, from_addr, body_text):
    """"
    Send An Email
    """
    BODY  = "\r\n".join((
        "From: %s" % from_addr,
        "To: %s" % to_addr,
        "Subject: %s" % Subject,
        ""
        body_text
    ))
    server = smtplib.SMTP(host)
    server.sendmail(from_addr, [to_addr],BODY)
    server.quit()

    if _name_=="main_":
        host = "mySMTP.server.com"
        subject = "Test email from Python"
        to_addr = "mike@someAddress.org"
        from_addr = "python@mydomain.com"
        body_text = "Python is the next language of choice"
        send_email(host, subject,to_addr, from_addr, body_text)

HOST = "mySMTP.server.com"
SUBJECT = "Testing email with python"
TO = "mike@someAddress.com"
FROM = "king@mydomain.com"
text = "Python is the bet language to use"

BODY = "\r\n". join(( # Using the join() method to combine all the previous variables into a single string
    # where each line ends with a carriage return("/r")
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
))

server = smtplib.SMTP(HOST)
server.login(username, password)  # If your server requires authentication
server.sendmail(FROM, [], BODY)
server.quit()

