import time
from celery import task
@task
def sendmail(mail):
    print ('sending mail to zzz..')
    time.sleep(2.0)
    print ('mail sent')
    print '************************'
    return mail