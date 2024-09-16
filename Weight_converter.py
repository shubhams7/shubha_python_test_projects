import numpy
times = int(input("how many people? "))
i=1
while  i<=times:
    weight = float(input("what is your weight? "))
    metric = input("the above weight is in kg(k/K) or   pounds(l/L)? ")
    if (metric=='K' or metric=='k'):
        print("your weight in pounds= " + str(weight*2.22) )
    else:
        print("your weight in kg is " + str(weight/2.22))
    i=i+1

