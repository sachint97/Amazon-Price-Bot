import requests
from bs4 import BeautifulSoup
import smtplib
import os

EMAIL = os.environ.get('python_email')
PASSWORD = os.environ.get('python_email_password')
URL="https://www.amazon.in/CASSIEY-Fashion-Slippers-slipper-design/dp/B09QXKN5X4/ref=sr_1_1_sspa?crid=2C6CIEGBMS2UU&keywords=slippers%2Bwomen%2Bstylish%2Bflat&qid=1650472909&sprefix=slippers%2Bwome%2Caps%2C566&sr=8-1-spons&smid=A3SED3NQ2J072W&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMEMzWDk4UEZDQVAyJmVuY3J5cHRlZElkPUEwOTUwNzczQUtCMjNEQUJZSVA2JmVuY3J5cHRlZEFkSWQ9QTA0MDc4NzYzUEhFQU41U1NYNjQ5JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1&psc=1"
HEADERS={
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
response=requests.get(url=URL,headers=HEADERS)

amazon_web=BeautifulSoup(response.text,"html.parser")
value_dollar=amazon_web.find(name="span",class_="a-offscreen").getText()
value=float(value_dollar.split("₹")[1])
title=amazon_web.find(name="span",class_="a-size-large product-title-word-break").getText()
product=title.strip()
if value<200:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(from_addr=EMAIL,
                        to_addrs=EMAIL,
                        msg=f"The Product {product} is at ₹{value} order quickly to get the deal ")

