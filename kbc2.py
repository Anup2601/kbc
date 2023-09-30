print("***** welcom to Kaun Banega Crorepati ***** ")
question=[
    [" What is the capital of France?","Berlin","Madrid", "Paris","London",3],
        [" What is the largest continent in the world?","Aisa","North America","South America","Europe",1]
          ]
levels=[1000,2000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,250000,5000000,10000000]
money=0
for i in range(0,len(question)):
    questions=question[i]
    print(f"question for rs{levels[i]}")
    print(f"1. {question[1]}\n2. {question[2]}")
    print(f"3. {question[3]}\n4. {question[4]}")
    reply=eval(input("enter your answer(1,2,3,4):"))
    if(reply==questions[-1]):
        print(f"your answer is correct you won{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
        else:
            print("wrong answer break")
            break

print(f"you take money at home is{money}")