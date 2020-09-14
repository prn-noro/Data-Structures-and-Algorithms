

def reverseString(string):
    if len(string)==0:
        return string
    else:
        final= reverseString(string[1:])+string[0]
        print(final)
        return final

string = 'i want to be reversed'

reversedString=reverseString(string)

print(reversedString)
