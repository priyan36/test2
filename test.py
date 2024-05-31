for i in range(int(input())):
    try:
        a,b=input().split()
        c=int(a)//int(b)
        print(c)
    except ZeroDivisionError as x:
        print("Error Code:",x)
    except ValueError as y:
        print("Error Code:",y)