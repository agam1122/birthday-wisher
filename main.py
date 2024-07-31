from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "your_email_id@gmail.com"
MY_PASSWORD = "your_app_password"


# Get the current date and time
today = datetime.now()
# Create a tuple with the current month and day
today_tuple = (today.month, today.day)

# Read the CSV file containing birthday information
data = pandas.read_csv("birthdays.csv")

# Create a dictionary where keys are tuples of (month, day) and values are the corresponding rows from the CSV
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today's date is in the dictionary of birthdays
if today_tuple in birthdays_dict:
    # Get the data for the birthday person
    birthday_person = birthdays_dict[today_tuple]
    # Choose a random letter template file from 3 available options
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # Open and read the chosen letter template file
    with open(file_path) as letter_file:
        contents = letter_file.read()
        # Replace the placeholder [NAME] with the actual name of the birthday person
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Set up the email connection
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(MY_EMAIL, MY_PASSWORD)  # Log in to the email account
        # Send the email
        connection.sendmail(
            from_addr=MY_EMAIL,  # Sender's email address
            to_addrs=birthday_person["email"],  # Recipient's email address
            msg=f"Subject:Happy Birthday!\n\n{contents}"  # Email subject and body
        )

# we can use pythonanywhere website to run our code at any time , daily etc...
