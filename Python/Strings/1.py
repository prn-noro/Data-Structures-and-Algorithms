# Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
# https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

string="i.like.this.program.very.much"
string="pqr.mno"
string=string.split(".")
string=string[::-1]

final=".".join(str(x) for x in string)
print(final)