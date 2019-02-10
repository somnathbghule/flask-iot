#!/usr/bin/python3

import os
from Emailer import Server 
from Emailer import EmailId 
from Emailer import MailSender 
import socket

class Support():
    def __init__(self, subject, body, attachments):
        self.__send_from=EmailId('somnath.bhaskar.ghule@gmail.com','Admin@123')
        self.__send_to=['somnath.bhaskar.ghule@gmail.com']
        self.__server=Server('smtp.gmail.com', 465)
        self.__subject=subject
        self.__attachments=attachments
        self.__body=body
        self.invoke()
    def invoke(self):
        sender=MailSender(self.__send_from,self.__send_to, self.__subject, self.__body,self.__attachments, self.__server)
        sender.send_mail();
    def supportLog():
        return os.path.dirname(os.path.abspath(__file__)) +"/../support_logs/iotsupport.log"
class Warn(Support):
    def __init__(self, warnId):
        self.__subject="Warning case [%d]" % warnId
        super().__init__(self.__subject, self.body(), [Support.supportLog()]) 
    def body(self):
        message="Hi Team,\nYour attention Required in Following case.  "
        return message

from datetime import datetime
months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
class LogDebug(Support):
    def __init__(self, message):
        fp = open(Support.supportLog(),"a")
        log=months[int(datetime.now().strftime("%m"))-1]+" "+datetime.now().strftime("%d %H:%M:%S") +" "+socket.gethostname()+" "+ message
        log+="\n"
        fp.write(log)
        fp.close()
        print (log)

if __name__ == '__main__':
    s=Warn(101)
