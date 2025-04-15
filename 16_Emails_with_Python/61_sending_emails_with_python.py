import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)
print(  smtp_object.ehlo()  )        # Greet/connect email server
print(  smtp_object .starttls()  )       # Starts TLS

email = getpass.getpass("Email: ")
password = getpass.getpass("Password please: ")     # We use the getpass library for a more secure way to get the users password through an input, if using gmail you need a special app password
print(smtp_object.login(email,password))    # Authenticate in the email server

# Building the email parameters
from_address = email
to_address = email
subject = input("Enter Subject Line:")
message = input("Enter the body message:")
msg = "Subject: "+subject+'\n'+message

print( smtp_object.sendmail(from_address,to_address,msg) )
smtp_object.quit()