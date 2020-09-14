# How do you print duplicate characters from a string

string='Great responsibility'

string=string.lower()
unique=set()
duplicate=set()
for i in string:
    if i not in unique:
        unique.add(i)
    else:
        duplicate.add(i)
    
print(duplicate)