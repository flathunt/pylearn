def ValidString (TestString):
    for character in TestString:
        if not (character.isalpha() or character == " "):
            return False
    return True

def HideText (MyString):
    Hidden =[]
    for character in MyString:
        if character == " ":
            Hidden.append("/")
        else:
            Hidden.append("*")
    return Hidden 

def IsInString (Test, MyString):
    for character in MyString:
        if character == Test:
            return True
    return False

def CopyLetters (Letter, Copy, Original):
    for character in range (0, len(Original)):
        if Original[character] == Letter:
            Copy[character] =Letter
    return Copy

def ShowList (MyString):
    print("".join(MyString))

def IsSolved (Answer):
    for character in Answer:
        if character == "*":
            return False
    return True

def TakeALife (LivesLeft):
    print("not in word you lose a life")
    LivesLeft = LivesLeft-1
    if LivesLeft <=0:
        print("Too bad, you lose the game")
    else:
        print("You have ", LivesLeft, " lives left")
    return LivesLeft

def ClearScreen():
    for count in range (20):
        print("\n")

#main program starts here
answer =input("Write a movie, book, famous person, song etc. ")
lives = 5

ClearScreen()

while not ValidString(answer):
    answer = input("not valid input, only write letters and spaces ")

attempt = HideText(answer)

while not IsSolved(attempt) and lives >0:
    print("solution so far is ")
    ShowList(attempt)

    letter = input("which letter are you choosing? ")

    if IsInString (letter,answer):
        attempt =CopyLetters(letter, attempt, answer)
    else:
        lives = TakeALife (lives)

if IsSolved(attempt):
    print("woop woop you are ah winna hoorah!")
