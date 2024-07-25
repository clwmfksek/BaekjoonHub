days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
l = []
for i in range(1,13):
    l.append(days[i] % 7)
a,b = map(int,input().split())
suml = 0
for i in range(0,a-1):
    suml += l[i]
suml += b%7
suml %= 7
weeks = ["SUN","MON", "TUE", "WED", "THU", "FRI", "SAT"]
print(weeks[suml])