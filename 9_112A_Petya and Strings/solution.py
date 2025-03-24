strings = []

for i in range(2):
    string = input()
    strings.append(string)

if strings[0].lower() > strings[1].lower():
    print(1)
elif strings[0].lower() < strings[1].lower():
    print(-1)
else:
    print(0)