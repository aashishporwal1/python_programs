from questions import quiz
print("WELCOME  TO QUIZ GAMING CHALLENGE")


while True:
    choice= int(input("""Select Your Role :
                      -> Quiz Master ( press 1 )
                      -> Quiz Cracker ( press 2 ) """))
    if choice == 1 :
        print("""" Welcome Master
        Shake Your Brain and Add Some Questions...
                Menu
        press 1 for add questions
        press 2 for view questions
        press 3 for delete questions
        press 4 for exit""")

        choice=int(input("Which Operations do you want to perform :"))
        if choice == 1:
            ques=input("Enter the question with options :")
            opt=[]
            print("Enter the four options with character initials (A,B,C,D)")
            for i in range(1,5):
                opt.append(input("Option"))
            ans=input("Enter the answer :")
            dict={"question":ques,"options":opt,"answer":ans}
            quiz.append(dict)
            print("Question Added Successfully")
            
        if choice == 2:
            for i in quiz:
                print(i)
            



                      
