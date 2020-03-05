def is_isogram(string):   
    exception=" ,_-"
    cont=[i.lower() for i in string if i not in exception]
    for i in cont:
     if cont.count(i)>1:
         return False
    else:
         return True