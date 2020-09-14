# How do you check if two strings are a rotation of each other

string1='ABCDE'
string2='CDABE'

# If two strings are not equal
if len(string1)!=len(string2):
    print("False")
else:
    # Concatinating the first string with itself
    tempString=string1+string1

    # Second string is a substring of first string
    if tempString.count(string2)!=0:
        print(True)

    # Other alterantive are, 1.)(if string2 in tempString)
    #                        2.)if(tempString.find(string2) == True)
    else:
        print(False)
