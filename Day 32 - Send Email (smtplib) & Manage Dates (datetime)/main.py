import random
import smtplib
import datetime as dt

sender = "donquixotee7@gmail.com"
password = "bswgnxjgujhytgrm"
# recipient = "sashabrause7@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        message = f"Subject:Monday Motivation\n\n{quote}"
        connection.starttls()
        connection.login(sender, password)
        connection.sendmail(from_addr=sender, to_addrs=sender, msg=message)