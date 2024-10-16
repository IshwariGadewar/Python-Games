import smtplib

# my_email = "eshwarigadewar24@gmail.com"
# password = "12345"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()

# connection.login(user=my_email,password=password)
# connection.sendmail(
#     from_addr=my_email,to_addrs="maitrimoreofficial@gmail.com",msg="Subject:hello\n\nThis is the bodt of mail"
# )
# connection.close()

import datetime

now = datetime.datetime.now()
year = now.year
month = now.month

birthdate = datetime.datetime(year=2004,month=5,day=24)

print(birthdate)

print(now)