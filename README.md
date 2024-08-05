# birthday-wisher

This Python script automatically sends a personalized birthday email to your friends or family members on their special day. The script reads birthday information from a CSV file and uses pre-written letter templates to generate the email content.


## How It Works

1. The script fetches the current date.
2. It checks if today's date matches any birthday in the CSV file.
3. If there's a match, it selects a random letter template.
4. The script customizes the template with the birthday person's name.
5. Finally, it sends an email using the Gmail SMTP server.


## Prerequisites

- Python 3.x
- `pandas` library
- `smtplib` library
- A Gmail account for sending emails

## Installation

1. Clone this repository:
    ```
    git clone https://github.com/agam1122/birthday-wisher.git
    cd birthday-wisher
    ```
    
2. Install the required Python libraries:
    ```
    pip install pandas
    ```

3. Prepare your `birthdays.csv` file in the following format:
    ```c
    name,email,year,month,day
    name1,example1@example.com,2004,7,28
    name1,example2@example.com,2005,7,29
    ```

4. Create a folder named `letter_templates` and add your letter templates as `letter_1.txt`, `letter_2.txt`, and `letter_3.txt`. Each template should contain `[NAME]` as a placeholder for the recipient's name.

5. Add your Gmail credentials to the script:
    ```
    MY_EMAIL = "your-email@gmail.com"
    MY_PASSWORD = "your-password"
    ```

## Scheduling
You can use a scheduling service like PythonAnywhere to run this script automatically at your desired intervals (e.g., daily).

