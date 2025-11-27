class flashcard:
    def __init__(self , word, meaning):
        self. word = word
        self.meaning = meaning

    def __str__(self):
        return self.word+'('+self.meaning+')'
    

flash = []
print("Welcome to flashcard aplication")
while(True):

    word = input("Enter te word that you want to name the flashcard:")
    meaning = input("Eneter the meaning of word" )

    flash.append(flashcard(word , meaning))
    option  = int(input("enter 0 , if you want to add an other flashcard otherwise enter 1:"))
    if option :
        break



print("\n Your Flashcards")
for i in flash:
    print(">" , i)






