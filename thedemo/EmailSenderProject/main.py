# import smtplib
#
#
# my_email = "example@gmail.com"
# password = "your_password"
#
#
#
# # creating smtplib object
# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
# # encrypted message to enhance security
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs= "reciever@gmail.com",
#                         msg="Subject: Hello World\n\n This is a test message")
#
#     # connection.close()


import datetime as dt

