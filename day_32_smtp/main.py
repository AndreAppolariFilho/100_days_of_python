import smtplib
import pandas as pd
import datetime
import datetime as dt
import random

my_email = "teste@gmail.com"
password = "password"

now = dt.datetime.now()

with open("quotes.txt") as data_file:
    quotes = [row.strip() for row in data_file.readlines()]
quote = random.choice(quotes)
if now.weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="receiver@gmail.com",
            msg=f"Subject:Motivation quote for the week\n\n{quote}"
        )

##################### Extra Hard Starting Project ######################



def get_letter():
    index = random.randint(1, 3)
    try:
        with open(f"letter_templates/letter_{index}.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""


# 1. Update the birthdays.csv
birthdays_df = pd.read_csv("birthdays.csv")
# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.datetime.now()
for i, row in birthdays_df.iterrows():
    row_day = datetime.datetime(year=row["year"], month=row["month"], day=row["day"])
    if row_day.day == today.day and row_day.month == today.month:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = get_letter()
        letter = letter.replace("[NAME]", row["name"])

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Happy Birthday {row['name']}\n\n{letter}"
            )