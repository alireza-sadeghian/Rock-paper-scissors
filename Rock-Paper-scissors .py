# بسم الله الرحمن الرحیم
import random as rand
yourScore = 0
compScore = 0

while(True):
    computer = rand.randint(1, 3)

    inp = input("قیچی سنگ کاغذ")
    if inp == "تمام" :
        break
    if computer == 1:
        comp = "سنگ"
    elif computer == 2 :
        comp = "کاغذ"
    elif computer == 3:
        comp = "قیچی"

    if comp == "سنگ" and inp == "کاغذ" :
        yourScore += 1
        barande = "شما"
    elif comp ==  "کاغذ" and inp == "سنگ" :
        compScore += 1
        barande = "کامپیوتر"
    elif comp == "سنگ" and inp == "قیچی" :
        compScore += 1
        barande = "کامپیوتر"
    elif comp == "قیچی" and inp == "سنگ" :
        yourScore += 1
        barande = "شما"
    elif comp  == "کاغذ" and inp == "قیچی" :
        yourScore += 1
        barande = "شما"
    elif comp == "قیچی" and inp == "کاغذ" :
        compScore += 1
        barande = "کامپیوتر"
    else :
        barande = "مساوی"
    # elif comp == inp:
    #     compScore += 0
    #     yourScore += 0
    
    print(f"شما : {inp}")
    print(f"کامپیوتر : {comp}")
    print(f"امتیاز شما : {yourScore}")
    print(f"امتیاز کامپیوتر : {compScore}")
    print(f"برنده این دست : {barande}")
#علیرضا صادفیان