import ssl
import smtplib

sender_address = "daystar.dev01@gmail.com"
receiver_address = "seancarpentermusic@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

# SSL #########################################
# port = 465 # for SSL
# password = input("Enter the password: ")

# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     try:
#         server.login("daystar.dev01@gmail.com", password)
#         server.sendmail(sender_address, receiver_address, message)
#         print("Success")
#     except:
#         print("Failure")
#################################################

port = 587 # for startTLS
smtp_server = "smtp.gmail.com"
password = input("Enter your password: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # can be omited
    server.starttls(context=context) # secure the connection
    server.ehlo() # can be omited
    server.login(sender_address, password)
    server.sendmail(sender_address, receiver_address, message)
    print("successful login")
except Exception as e:
    # print any error messages to stdout
    print(e)
finally:
    server.quit()