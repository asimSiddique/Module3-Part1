
list=[]
total=0
x=1
while(x<=5):
    try:
        user_input=input(f"Enter int #{x}: ")
        list.append(int(user_input))
        x=x+1
    except ValueError:
        print("Invalid number. please enter an int ")
        continue
for ele in range(0, len(list)):
    total = total+list[ele]
print(f"Your sum is {total}")

