def factors(number):
    factores=[] 
    n=2
    while number>1:
        while (number%n) == 0:
            factores.append(n)
            number/=n
        n+=1
    return factores