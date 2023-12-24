from time import sleep
from random import randrange

while True:
    # Random number is used to "ilustrate a message from somewhere externally"
    random_number = randrange(0, 10)
    if random_number == 1:
        print("Received the message we expected")
        break
    # The message was not received
    # Wait a bit before requesting or proecessing a new message
    sleep(1)

# Alternative, without break

message_received = False
while not message_received:
    # Random number is used to "ilustrate a message from somewhere externally"
    random_number = randrange(0, 10)
    if random_number == 1:
        print("Received the message we expected")
        message_received = True
    # Not using else here will make us wait one more second before finishing the loop
    else:
        # The message was not received
        # Wait a bit before requesting or proecessing a new message
        sleep(1)
