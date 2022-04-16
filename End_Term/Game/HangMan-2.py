def Hangman(word,target) :
    find = ""
    for i in range (0,len(word)):
        if word.count(target[i]) >= 2 and target[i] not in find:
                find += target[i]
        if word[i] not in target :
            find += word[i]
    check = 4
    while check != 0:    
        In = str(input(f"Guess the word ? Chances Left - {check} : "))
        if In in find:
            for i in range (0,len(word)):
                if word[i] == In:
                    target[i] = In
            r = ""
            for i in range (0,len(target)):
                r += target[i]
            print (r)
            if target == word :
                print("You Won !!")
                break
        else :
            print("Wrong Answer !!")
            check -= 1
    else :
        print("You Lose !! HangMan !!")

# Main Page

words = ["hello","python","breaker"]
targets = ["h_l__","_yth__","____ke_"]
S = 0
while S != 4:    
    print("What difficult level you want to play ? (1-3) : ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Exit")
    S = int(input())
    if S == 1:
        word = list(words[0])
        target = list(targets[0])
        r = ""
        for i in range (0,len(target)):
            r += target[i]
        print(r)
        Hangman(word,target)
    elif S == 2:
        word = list(words[1])
        target = list(targets[1])
        r = ""
        for i in range (0,len(target)):
            r += target[i]
        print(r)
        Hangman(word,target)
    elif S == 3:
        word = list(words[2])
        target = list(targets[2])
        r = ""
        for i in range (0,len(target)):
            r += target[i]
        print(r)
        Hangman(word,target)
    else :
        print("Thanks for playing...")