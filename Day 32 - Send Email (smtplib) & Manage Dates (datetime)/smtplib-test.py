import smtplib

sender = "donquixotee7@gmail.com"
password = "bswgnxjgujhytgrm"

recipient = "sashabrause7@gmail.com"
message = """Subject:Testing SMTLIB with Python\n\n
Pesan ini dikirim melalui smtplib dan diterima oleh modul SMTP Server Python."""

print(message)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(sender, password)
    connection.sendmail(sender, recipient, message)