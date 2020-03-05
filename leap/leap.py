def leap_year(año):
    año=int(año)
    if (año%4)!=0:
        return False
    if (año%100)==0 and (año%400)!=0:
        return False
    return True