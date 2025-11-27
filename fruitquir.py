import random
class FruitQuiz:

    def __init__(self):
        self . fruits = {'apple:', 'mango:', 'grape:', 'orange:', 'kiwi:', 'dragon fruit:', "'passion fruit:", 'raspberrry:'}
    def quiz(self):
        while(True):
            fruit, color = random.choice(list(self.fruits.items))
            print("hat is color of{}".format(fruit))
            user_answer = input()
            if(user_answer.lower()== color):
                print("Correct answer")


            else:


                print("Wrong answer")


                option = int(input("enter 0, if you want to play again othaerwise enter 1:"))
                
                if (option):
                    break

print(" Welcome to fruit quiz")
fq = FruitQuiz()
fq.quiz()




