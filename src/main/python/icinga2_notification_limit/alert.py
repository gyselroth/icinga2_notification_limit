from email.mime.text import MIMEText
from subprocess import Popen, PIPE

class EmailAlert(object):
    def __init__(self, recipient, message):
        msg = MIMEText(message)
        msg["Subject"] = "Icinga2 Notification Limit"
        p = Popen(["/usr/sbin/sendmail", recipient], stdin=PIPE)
        p.communicate(msg.as_string())
