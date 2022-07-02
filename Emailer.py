import smtplib

# This automation can send and check your email inbox

# conn is a connection object
# for the smtp server that is the domain name of your email pass "smtp.<DOMAIN NAME>.com"as argument
# and pass the port number for your smtp server
conn = smtplib.SMTP("smtp.gmail.com", 587)

# ehlo() establishes connection with the server and returns a connections status tuple
connection = conn.ehlo()
print(connection)

# starttls() encrypts the passwords which should be done before logging in
data_encryption = conn.starttls()
print(data_encryption)

user_email = input("Enter your email")
user_password = input("Enter your Password")

# 2-step verification should be disabled and 'less secure app access should be enabled' to successfully login in

conn.login(user_email, user_password)
conn.sendmail(user_email, input("Enter recipient's address"), "Test email 123098")
conn.quit()
