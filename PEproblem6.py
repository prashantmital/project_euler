x = 1;
sumsq = 0;
sumall = 0;
while(x<=100):
    sumsq = sumsq + x**2;
    sumall = sumall + x;
    x = x+1;
sumallsq = sumall**2;
difference = sumallsq-sumsq;
print(difference);