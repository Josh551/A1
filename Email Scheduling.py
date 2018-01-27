import smtplib
print("Welcome to the E-mail scheduling app.")
sender=input("Please Enter your G-Mail ID: ")
reciever=input("Please Enter the E-Mail you are sending to: ")
p=input('Enter your password: ')    #password input
print("Trying to login.....")
try:
    username=sender.split('@')
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(username[0],str(p))
    msg=input("Enter your message: ")
    server.sendmail(str(sender),str(reciever),msg)
    server.close()
except:
    print("E-mail not sent/Login Failed.")
else:
    print("Succesfully sent!")
