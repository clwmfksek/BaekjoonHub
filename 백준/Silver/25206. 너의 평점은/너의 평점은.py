count = 0
average = 0
while(1):
    try :
        t,num,gra = input().split()
        
        num = int(num.split(".")[0])

        if gra!="P":
            count += num

        if gra == "A+":
            average += num*45
        elif gra == "A0":
            average += num*40
        elif gra == "B+":
            average += num*35
        elif gra == "B0":
            average += num*30
        elif gra == "C+":
            average += num*25
        elif gra == "C0":
            average += num*20
        elif gra == "D+":
            average += num*15
        elif gra == "D0":
            average += num*10
    except :
        print((average/10)/count)
        break