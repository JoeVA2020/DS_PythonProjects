sub1=int(input("Subject 1 Marks"))
sub2=int(input("Subject 2 Marks"))
sub3=int(input("Subject 3 Marks"))
sub4=int(input("Subject 4 Marks"))

total=sub1+sub2+sub3+sub4

print("Total marks is",total)
if total >= 180:
    print("Grade is A+")
elif total>=160:
    print("Grade is A")
elif total>=140:
    print("Grade is B+")
elif total>=120:
    print("Grade is B")
elif total>=100:
    print("Grade is C+")
elif total>=80:
    print("Grade is C")
else:
    print("FAIL")