#!/usr/bin/python3

from Emailer import Server 
from Emailer import EmailId 
from Emailer import MailSender 

class Support():
    def __init__(self, subject, body, attachments):
        self.__send_from=EmailId('somnath.bhaskar.ghule@gmail.com','Admin@123')
        self.__send_to=['somnathbghule@gmail.com']
        self.__server=Server('smtp.gmail.com', 465)
        self.__subject=subject
        self.__attachments=attachments
        self.__body=body
        self.invoke()
    def invoke(self):
        sender=MailSender(self.__send_from,self.__send_to, self.__subject, self.__body,self.__attachments, self.__server)
        sender.send_mail();

class Warn(Support):
    def __init__(self, warnId):
        self.__subject="Warning case [%d]" % warnId
        super().__init__(self.__subject, self.body(), ["test.txt"]) 
    def body(self):
        message="Hi Team,\nYour attention Required in Following case.  "
        return message

if __name__ == '__main__':
    s=Warn(101)
