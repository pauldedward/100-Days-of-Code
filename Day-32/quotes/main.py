import smtplib
import os
import datetime as dt
import random
from dotenv import load_dotenv
load_dotenv()

my_email = os.getenv("EMAIL")
my_password = os.getenv('PASSWORD')

# with smtplib.SMTP('smtp.gmail.com', 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs=os.getenv("TO"), 
#         msg='Subject: Hello from Python\n\nBody of mail')

#     print('Mail sent successfully')

# now = dt.datetime.now()
# print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.weekday())

day = dt.datetime.today().weekday()

if day == 4:
    with open('quotes.txt') as f:
        quotes = f.readlines()
        random_quote = random.choice(quotes)
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=os.getenv("TO"), 
                msg=f'Subject: Monday motivation\n\n{random_quote}')

            print('Mail sent successfully')