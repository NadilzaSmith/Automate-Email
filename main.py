import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
tday = (now.month, now.day)

bday_info = pandas.read_csv("birthdays.csv")

bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in bday_info.iterrows()}
if tday in bday_dict:
    bday_person = bday_dict[tday]
    bday_letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(bday_letter) as letter_file:
        bday_c = letter_file.read()
        bday_c = bday_c.replace("[NAME]",bday_person["name"])

    email = "pychar.teste@gmail.com"
    password = "glgjlnkioffmyjwl"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=bday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{bday_c}"
        )