import random
tries=0
playerWord=""
wordsList=[
    "gioia"
    # "anatra",
    # "mulo",
    # "archibugio"
    ]
# choosenWord=str(wordsList[random.randint(0,len(wordsList)-1)]).upper()
# print(f"la parola scelta è {choosenWord}")

playground=[]

play=True

#this function takes the first word and pushes into the list the single chars and open spaces for layout
def start(word: str):
    listedWord=[]
    openSpace=[]
    for x in range(len(word)):
        listedWord.append(word[x])
        openSpace.append("")
    playground.append(listedWord)
    playground.append(openSpace)

# creates a list of a word to append into the playground (bidimensional list) used for layout
def appendWord(word):
    listedWord=[]
    for x in range(len(word)):
        listedWord.append(word[x])
    playground.append(listedWord)

# creates the spaces to append into the playground
def spaces(lenght: str):
    wrapper=""
    for x in range(len(lenght)):
        wrapper+=" "
    return wrapper    


#used to create the layout reading the bidim.list playground
def read():
    for c in range(len(playground)):
    
        for i in range(len(choosenWord)):
            #the first list into the list is the choosen word so we skip the printing
            if c>=1:
                #in this way we are reading only not spaced lists into the array
                if c%2!=0:
                    
                    if i == 0 :
                        print("||", end='')

                    if playground[c][i]=="":
                        print(f"   |", end='')
                    else :
                        print(f" {playground[c][i]} |", end='')
                    
                    if i == (len(choosenWord)-1): 
                        print("|")
                #here we read the spaces, that we are filling with the clues afterward
                if c%2==0:

                    if i == 0 :
                        #color white 
                        print(" \033[37m-", end='')

                    if i==(len(choosenWord)-1):
                        #if we have written v means the char is in the word and in correct position. color green
                        if playground[c][i]=="v":
                            print(f" \033[32m{playground[c][i]} ", end='')
                        #c means char is in the word but another position. color yellow
                        elif playground[c][i]=="c":
                            print(f" \033[33m{playground[c][i]} ", end='')
                        #x means char is not present in the word. color red
                        elif playground[c][i]=="x":
                            print(f" \033[31m{playground[c][i]} ", end='')
                        else:
                            print(f" {playground[c][i]} |", end='')
                        
                    else :
                        if playground[c][i]=="v":
                            print(f" \033[32m{playground[c][i]} \033[37m|", end='')
                        elif playground[c][i]=="c":
                            print(f" \033[33m{playground[c][i]} \033[37m|", end='')
                        elif playground[c][i]=="x":
                            print(f" \033[31m{playground[c][i]} \033[37m|", end='')
                        else:
                            print(f" {playground[c][i]} |", end='')
                    
                    if i == (len(choosenWord)-1): 
                        print("\033[37m- ")

#this checks the word and writes our control list.
def checkW(standard: str,userW: str):
    controlList=[]
    victory=0
    for i in range(len(userW)):
        #if we don't ever meet our char the basic control is x
        control="x"
        for c in range(len(standard)):
            #if i==c and the chars are the same means the char is rightand in correct position. Victory is used to see when a player wins.
            if i==c:
                if userW[i]==standard[c]:

                    control="v"
                    victory+=1
                    
            else:
                #char is in the word but in another position. the control!=v is to debug cases of double chars: xxaxx on input. xxaxa word to discorver: if we don't make this control this function would write V on the control when reading the first a and overwrite V with C when reading the second a.

                if userW[i]==standard[c] and control!="v":
                    
                    control="c"
        #we finally append our control into a list to push into playground.
        if control=="x":
            controlList.append("x")
        elif control=="c":
            controlList.append("c")
        elif control=="v":
            controlList.append("v")
    if victory==len(standard):
        return "ok"
    return controlList

#this function asks the input and makes a check for the legth of the written word
def insertWord():
    global playerWord
    check=False
    while check!=True:
    
        playerWord=str(input(f"\n prova a indovinare... ({len(choosenWord)} lettere)")).upper()
        if len(choosenWord)==len(playerWord):
            check=True
        else:
            print(f"la tua parola non era di {len(choosenWord)} lettere")

#this function is a round, calling all the previous functions in the logical order
def round():
    global playground                    
    playground=[]
    #makes the list of chars of the choosen word and the spaces list and pushes into the playground
    start(choosenWord)
    #tries makes the maximum number of times a player can guess the word, play is set when finishing a round if u want to pòlay again or not
    tries =0
    while tries<=6 or play==False:
        #takes the input word
        insertWord()
        # #shows the playground with only empty boxes
        # print(playground)
        #this pops the spaces list before appending the user input word
        playground.pop((tries*2)+1)
        tries+=1
        appendWord(playerWord)
        #the function checkW writes the int array, but also returns ok if all the chars are correct 
        if (checkW(choosenWord,playerWord))=="ok":
            print(f"vittoria, hai effettuato {tries} tentativi!")
            
            break
        playground.append(checkW(choosenWord,playerWord))
        # print(checkW(choosenWord,playerWord))
        appendWord(spaces(choosenWord))
        print(playground)
    
        #here we give the layout with the ints and the user input word
        read()

#here we put all together, to finally run the game.
while play != False:
    #we take the choosen word with a random number
    wordIndex=random.randint(0,len(wordsList)-1)
    choosenWord=str(wordsList[wordIndex]).upper()
    # print(f"la parola scelta è {choosenWord}")
    #then we play the round with the word
    round()
    #then we ask if the user wants to play again 
    goesOn=""
    while goesOn!="Y" and goesOn!="N":
        goesOn=str(input(f"\n vuoi continuare a giocare? y/n\n")).upper()
    if goesOn=="N":
        play=False
    else:
        #if the player wants to play again we pop the last choosen word from the list so we can't get it again with the random number
        wordsList.pop(wordIndex)
        print(wordsList)
   
