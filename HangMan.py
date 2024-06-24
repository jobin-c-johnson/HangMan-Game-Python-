word= input("Enter the word : ")        #if you need it hidden create an default words list
word=[*word]
count=len(word)
print(f"It has {count} letters")
while(count!=0):
    guess= input("\nEnter the guess letter : ")
    if guess in word:
        print("Correct guess")
        word.remove(guess)
        if len(word)==0:
            print("\nYou won the game\n")
            break
    else:
        print("Incorrect")
        count=count-1   
if count==0:
    print("\nGame Over\n")
