import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email@gmail.com", "your_password")

message = "Hello, this is an automated email!"
server.sendmail("your_email@gmail.com", "receiver_email@gmail.com", message)
server.quit()
