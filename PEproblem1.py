num = 1;
add = 0;
while(num<1000):
    if num%3==0 or num%5==0:
        print(num);
        add = add+num;
    num=num+1;
print('The sum is =',add);