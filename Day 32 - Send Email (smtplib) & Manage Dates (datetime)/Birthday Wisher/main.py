##################### Normal Starting Project ######################
import random
import pandas
import smtplib
from datetime import datetime

sender = "donquixotee7@gmail.com"
password = "bswgnxjgujhytgrm"
today = (datetime.now().month, datetime.now().day)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
#Dictionary comprehension template for pandas DataFrame looks like this:
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today in birthdays_dict:
    # 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today]
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        message = f"Subject:Happy Birthday!\n\n{content}"
        connection.starttls()
        connection.login(sender, password)
        connection.sendmail(from_addr=sender, to_addrs=birthday_person["email"], msg=message)