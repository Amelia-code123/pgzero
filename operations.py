s=set(input("Enter the set elements separated by a space: "))
ss=set(input("Enter the second set elements separated by a space: "))
print(s)
print(ss)
while True:
    print("MENU: \n 1.Union \n 2.Intersection \n 3.Difference \n 4.Symetric Difference \n 5.Exit")
    choice=int(input("Choose an option: "))

    if choice==1:
        print(s|ss)
    elif choice==2:
        print(s&ss)
    elif choice==3:
        print(s-ss)
    elif choice==4:
        print(s^ss)
    elif choice==5:
        break
