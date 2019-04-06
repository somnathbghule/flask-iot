#!/usr/bin/python3

import os
from Emailer import Server 
from Emailer import EmailId 
from Emailer import MailSender 
import socket
import platform
import time
from datetime import datetime, timedelta

class Support():
    supportLogDir_ = '/var/log/iosupport'
    supportLogF_= supportLogDir_ + '/iotsupport.log.0'
    supportBundle=[supportLogF_]
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
    def isLogRotate():
        fileCreation = datetime.fromtimestamp(os.path.getctime(Support.supportLogF_))
        oneday_ago = datetime.now()
        if int(fileCreation.strftime('%d%m')) < int(oneday_ago.strftime('%d%m')):
                return True
        return False
    def logRotate():
        dir = Support.supportLogDir_ 
        files = os.listdir(dir)
        if not Support.supportBundle:
            for srcFile in sorted(files, reverse=True):
                Support.supportBundle.append(dir+"/"+srcFile)
        if not Support.isLogRotate():
            return False
        Support.supportBundle = [Support.supportLogF_]
        for srcFile in sorted(files, reverse=True):
            fCount=int(srcFile[-1:])
            destFile=srcFile[:-1]+str(fCount+1)
            if fCount>=5:
               os.remove(dir+"/"+srcFile)
               continue
            os.rename(dir+"/"+srcFile,dir+"/"+destFile)
            Support.supportBundle.append(dir+"/"+destFile)

        open(Support.supportLogF_, 'a').close()
        return True

    def supportLog():
        if Support.logRotate() :
            LogDebug("logRotate() done.")
        return Support.supportLogF_

class Warn(Support):
    def __init__(self, warnId):
        self.__subject="Warning case [%d]" % warnId
        if not Support.supportBundle:
            LogDebug ("Support Bundle is empty")
        super().__init__(self.__subject, self.body(),Support.supportBundle) 
    def body(self):
        message="Hi Team,\nYour attention Required in Following case.  "
        return message

months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
class LogDebug(Support):
    def __init__(self, message):
        fp = open(Support.supportLog(),"a")
        message = "\""+str(message)+"\""
        log="["
        log+=months[int(datetime.now().strftime("%m"))-1]+" "+datetime.now().strftime("%d %H:%M:%S") +"] "+socket.gethostname()+" "+ message
        log+="\n"
        fp.write(log)
        fp.close()
        print (log)
if __name__ == '__main__':
    LogDebug("IoTSupport Called.")
    s=Warn(101)
