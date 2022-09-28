def draw_hangman(wrong,board):
     
    if wrong == 0:
        print(board)
         
    elif wrong == 1:
        print ("     ______")
        print ("    |/")
        print ("    |")
        print ("    |")
        print ("    |")
        print ("   _|_")
        print(board)
 
    elif wrong == 2:       
        print ("     ______")
        print ("    |/")
        print ("    |   o  ")
        print ("    |")
        print ("    |")
        print ("   _|_")
        print(board)   
    elif wrong == 3:       
        print ("     ______")
        print ("    |/")
        print ("    |   o  ")
        print ("    |   |")
        print ("    |")
        print ("   _|_")
        print(board)   
    elif wrong == 4:       
        print ("     ______")
        print ("    |/")
        print ("    |  _o  ")
        print ("    |   |")
        print ("    |")
        print ("   _|_")
        print(board) 
    elif wrong == 5:       
        print ("     ______")
        print ("    |/")
        print ("    |  o ")
        print ("    |   |")
        print ("    |")
        print ("    |")
        print ("    |")
        print(board) 
    elif wrong == 6:       
        print ("     ______")
        print ("    |/")
        print ("    |  o ")
        print ("    |   |")
        print ("    |  /")
        print ("   _|_")
        print(board)   
    elif wrong == 7:       
        print ("     ______")
        print ("    |/")
        print ("    |  o ")
        print ("    |   |")
        print ("    |  / \\")
        print ("   _|_")
         
    elif wrong == 8:
        print ("     ______")
        print ("    |/  |")
        print ("    |  o ")
        print ("    |   |")
        print ("    |  / \\")
        print ("   _|_")
        print(board)
        print("hangman! game over!")     
         
def get_letter(guesses):
 
    ok = True
    while ok:    
        try:
            letter = input("enter your letter:")
            if letter in guesses:
                print("already used,try again")
            elif not letter.isalpha():
                print("not a valid letter")
            elif len(letter) == 1:
                letter = letter.lower()
                break
        except:
            print("try again")
    return letter        
        
def set_up():
 
    ok = True
    while ok:    
        try:
            answer = input("enter your word or phrase:")
 
            if not answer.isalpha():
                if " " in answer:
                    temp = answer.replace(" ","")
                    if temp.isalpha():
                        answer = answer.lower() 
                        break
                print("only enter words not numbers or punctuation")
            else:
                answer = answer.lower()
                break
        except:
            print("try again")
                        
    #create board    
    board = ""
    for ch in answer:
        if ch == " ":
            board = board + " "
        else:
            board = board + "-"
     
    return answer,board   
 
def check_guess(answer,board,letter,wrong):
 
    if letter not in answer:
        wrong = wrong + 1 
    else:
        for i in range(len(answer)):
            if answer[i] == letter:
                board = board[:i] + letter + board[i+1:]
    return board,wrong
             
answer,board = set_up()
guesses = ""
wrong = 0
 
for i in range(27):
    letter = get_letter(guesses)
    guesses = guesses + letter
    board,wrong = check_guess(answer,board,letter,wrong)
    draw_hangman(wrong,board)
    if board == answer:
        print("you win")
        break
    elif wrong == 8:
        break