#Program to print prime numbers from 0 to 100
x=2

while(x<=100):
    flag=0
    for i in range(2, x):
        if(x%i==0):
            flag+=1
    if(flag==0):
        print(x)
    x+=1
    
        
