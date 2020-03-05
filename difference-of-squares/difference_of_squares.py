def square_of_sum(number):
    cont=list(range(1,number+1))
    sumcont=sum(cont)
    return (sumcont**2)

def sum_of_squares(number):
    cont=list(range(1,number+1))
    sumcont=0
    for i in range(len(cont)):
        sumcont+=(cont[i]**2)
    return sumcont

def difference_of_squares(number):
    return(square_of_sum(number)-sum_of_squares(number))
    