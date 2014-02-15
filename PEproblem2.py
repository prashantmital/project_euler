t1 = 1;
t2 = 2;
tot = 2;
while(t1<4000000 and t2<4000000):
    t3 = t1+t2;
    t4 = t3+t2;
    if t3%2==0:
        tot = tot+t3;
    if t4%2==0:
        tot = tot+t4;
    t1 = t3;
    t2 = t4;
print('END');
print(tot);
