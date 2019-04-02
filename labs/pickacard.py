import showcard
showcard.set_timeout(1)
number = input("Pick a card (1-52): ")
showcard.display_file('BMP' + number + '.GIF')