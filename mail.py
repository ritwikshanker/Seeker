import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

# Next, log in to the server
server.login("youremailusername", "password")

# Send the mail
msg = "Hello!"  # The /n separates the message from the headers
server.sendmail("you@gmail.com", "target@example.com", msg)
