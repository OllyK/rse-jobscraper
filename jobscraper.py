import smtplib
import ssl
from datetime import date
from base64 import b64decode

from email_info import details
from utils import get_webdriver
from lightsources_job_finder import LightsourceJobFinder
from merck_job_finder import MerckJobFinder
from msd_job_finder import MSDJobFinder
from novo_nordisk_job_finder import NovoNordiskJobFinder
from ox_uni_job_finder import OxUniJobFinder
from rosalind_job_finder import RosalindJobFinder

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = b64decode(details[0]).decode('utf-8')  # Enter your address
receiver_email = b64decode(details[1]).decode('utf-8')  # Enter receiver address
password = b64decode(details[2]).decode('utf-8')

OUT_FILE = "Jobs_list.txt"

# Setup selenium driver for those that need it
driver = get_webdriver()

ox_uni = OxUniJobFinder()
ros_frank = RosalindJobFinder(driver)
msd = MSDJobFinder(driver)
lights = LightsourceJobFinder(driver)
merck = MerckJobFinder(driver)
novo_nord = NovoNordiskJobFinder(driver)

job_finders = [ox_uni, ros_frank, msd, lights, merck, novo_nord]
message = f"""\
Subject: Bumper job search results for {date.today()}.

This message is sent from Python.\n\n"""

with open(OUT_FILE, 'w', encoding='utf-8') as f:
    for job_finder in job_finders:
        text = job_finder.find_jobs() + "\n"
        f.write(text)
        message += text
print(f"Jobs writtten out to {OUT_FILE}")
# Close the selenium browser
driver.quit()

# Send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.encode('utf-8'))

print("Check your email!")
