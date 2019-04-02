import getpass

pin = 9293
attempts = 3

for tryo in range(0, attempts):
    guess = int(getpass.getpass("Enter 4 digit PIN: ")[:4])
    if guess == pin:
        print("Success! You had", tryo, "failed attempts")
        break
    else:
        print("Incorrect.")