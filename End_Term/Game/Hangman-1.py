def level1():    
    print("Level - 1")
    Find = "_ _ t h _ n" # p y t h o n
    print (Find)
    p = False
    y = False
    o = False
    i = 5
    while i != 0:
        In = str(input(f"Guess The Letter ? Chances Left : {i}"))
        if In.lower() == "p":
            p = True
        elif In.lower() == "y":
            y = True
        elif In.lower() == "o":
            o = True
        else :
            i -= 1
        if  p and y and o :
            print("p y t h o n")
            print("You Won !!")
            Won = True
            return Won
            break
        elif p and y :
            print("p y t h _ n")
        elif p and o :
            print("p _ t h o n")
        elif o and y :
            print ("_ y t h o n")
        elif p :
            print("p _ t h _ n")
        elif y :
            print("_ y t h _ n")
        elif o :
            print("_ _ t h o n")
    else :
        print("You Lose !!")
        Won = False
        return Won
def level2():
    print("Level - 2")
    Find = "_ _ e" # i c e
    print(Find)
    i = False
    c = False
    k = 5
    while k != 0:
        In = str(input(f"Guess The Letter ? Chances Left : {k}"))
        if In.lower() == "i":
            i = True
        elif In.lower() == "c":
            c = True
        else :
            k -= 1
        if  i and c :
            print("i c e")
            print("You Won !!")
            Won = True
            return Won
            break
        elif i :
            print("i _ e")
        elif c :
            print("_ c e")
    else :
        print("You Lose !!")
        Won = False
        return Won
def level3():
    print("Level - 3")
    Find = "_ k _" # s k y
    print(Find)
    s = False
    y = False
    j = 5
    while j != 0:
        In = str(input(f"Guess The Letter ? Chances Left : {j}"))
        if In.lower() == "s":
            s = True
        elif In.lower() == "y":
            y = True
        else :
            j -= 1
        if  s and y :
            print("s k y")
            print("You Won !!")
            Won = True
            return Won
            break
        elif s :
            print("s k _")
        elif y :
            print("_ k y")
    else :
        print("You Lose !!")
        Won = False
        return Won
print ("!! Welcome to Hangman Game !!")
while True :    
    if level1() :
        level2()
        if level2() :
            level3()
        else :
            level2()
    else :
        level1()
    
        
