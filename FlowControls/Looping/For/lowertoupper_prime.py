lower=int(input('Enter lower limit : '))
upper=int(input('Enter upper limit : '))
for i in range(lower,upper):
        flag=0
        for j in range(2,lower):
            if(lower%j==0):
                flag=1
                lower+=1
                break
        if(flag==0):
                print(lower,'is prime')
                lower+=1



