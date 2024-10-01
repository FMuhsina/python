ch=int(input("enter the choice (1.circle/2.rectangle/3.triangle):"))
if ch==1 :
    r=int(input("Enter the radius of circle :"))
    area=3.14*r*r
    print(area)
elif ch==2 :
    l=int(input("Enter the length of rectangle :"))
    b=int(input("Enter the breadth of rectangle :"))
    area=l*b
    print(area)
elif ch==3 :
    h=int(input("Enter the height of triabgle :"))
    b=int(input("Enter the base of triangle :"))
    area=0.5*b*h
    print(area)
else :
    print("invalid choice")
