import smtplib

my_email = "rahulch19905@gmail.com"
password = ""

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="rahulch19905@yahoo.com",msg="Hello")
connection.close()