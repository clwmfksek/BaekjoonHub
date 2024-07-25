inp = int(input())

if inp%4 == 0 and inp%100 != 0 or inp%400 == 0: print("1")
else : print("0")