import json
print("WELCOME  TO QUIZ GAMING CHALLENGE")


while True:
    main_choice= int(input("""Select Your Role :
                      -> Quiz Master ( press 1 )
                      -> Quiz Cracker ( press 2 ) """))
    
    if main_choice == 1 :
        print(""" Welcome Master
        Shake Your Brain and Add Some Questions...
                Menu
        press 1 for add questions
        press 2 for view questions
        press 3 for delete questions
        press 4 for exit""")

        choice=int(input("Which Operations do you want to perform :"))
        while True:
            if choice == 1:
                ques=input("Enter the question with options :")
                opt=[]
                print("Enter the four options with character initials (A,B,C,D)")
                for i in range(1,5):
                    opt.append(input("Option"))
                ans=input("Enter the answer :")
                dic={"question":ques,"options":opt,"answer":ans}
                
                with open("questions.json","r+") as f :
                    questions = json.load(f)
                    questions.append(dic)
                    f.seek(0)                
                    json.dump(questions,f)
                    f.truncate()
                    print("Question Added Successfully")
                
            if choice == 2:
                with open("questions.json","r") as f:
                    questions = json.load(f)
                    print("All the questions are as follow :")
                    for i in questions:
                        print(i["question"])
                continue
            
            if choice == 3:
                
                with open("questions.json","r",encoding='utf-8') as file:
                    data=json.load(file)
                
                ques = input("Enter the question you want to delete :")       
                    
                for item in data:
                    if item['question'] == ques :
                        data.remove(item)
                        break
                else:
                    print("Question does not exist")
                    break
                
                
                with open("questions.json","w") as file:
                    json.dump(data , file , indent=4)
                
            if choice == 4 :
                break
                
                
                      
