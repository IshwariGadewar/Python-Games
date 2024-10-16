import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday==6:
    with open("D:\PYTHON\PYTHON - Udemy\Game\Automated Birthday Wisher\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)