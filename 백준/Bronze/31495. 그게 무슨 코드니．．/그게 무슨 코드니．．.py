inp = input()

if inp[0] != '"' or inp[-1] != '"' or len(inp) < 3:
    print('CE')
else:
    print(inp[1:-1])