string = input("Please enter your own word")
char = input("Please entrt your own character: ")
i = 0
count = 0
while (i < len (string) ): 
    if (string[i] == char  ):
        count = count + 1
        i = i + 1
        print("The total Number of Times " ,char , "has Occured = " ,count )

