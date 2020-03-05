def find_anagrams(a, b):
    return [n for n in b 
            if n.lower()!=a.lower() 
            and sorted(n.lower())==sorted(a.lower())]