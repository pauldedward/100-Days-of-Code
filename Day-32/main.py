import smtplib
import os
import pandas as pd
import datetime as dt
from dotenv import load_dotenv
load_dotenv()

today = dt.datetime.today()
this_date = today.day
this_month = today.month
birthday_list = pd.read_csv('birthdays.csv')

for i in range(len(birthday_list)):
    if int(this_month) == int(birthday_list['month'][i]) and int(this_date) == int(birthday_list['day'][i]):
        
        print(f'Happy Birthday {birthday_list["name"][i]}!')
    
        try:
            message = f'Subject:Happy Birthday!\n\nDear {birthday_list["name"][i]}!\nIt\'s your birthday! I wish you to enjoy this day and be happy forever.\n\nWith Perennial Love,\nEdward'
            
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))
                connection.sendmail(os.getenv('EMAIL'), birthday_list['email'][i], message)
            print(f'Email sent to {birthday_list["name"][i]}')

        except Exception as e:
            print(f'Email failed to send to {birthday_list["name"][i]}\n{e}')




