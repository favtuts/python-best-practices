a = [1,2,3]
b = [3,4,5]
c1 = [*a,*b]
c2 = [a,b]

dict1 = {'a':1,'b':2}
dict2 = {'b':2,'c':3}
dict3 = {**dict1,**dict2}

# c1:[1, 2, 3, 3, 4, 5]
# c2:[[1, 2, 3], [3, 4, 5]]
print(f"c1:{c1}\n c2:{c2}")

# {'a': 1, 'b': 2, 'c': 3}
print(dict3)