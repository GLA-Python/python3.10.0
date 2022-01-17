import re
'''
Regular Expression is a sequence of characters that forms a search pattern in a String.
In another words this is scheme for Advance Search operation on string.

The "re" package provides several methods to actually perform queries on an input string
1. re.search() : Returns a Match object if there is a match anywhere in the string
2. re.match() : returns a match object on success, None on failure
3. re.findall() : Returns a list containing all matches
4. re.sub() : Replaces one or many matches with a string
5. re.split() : Returns a list where the string has been split at each match
6. re.compile() : We can combine a regular expression pattern into pattern objects,
                  which can be used for pattern matching.
                  It also helps to search a pattern again without rewriting it'''

# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:
# import re


# 1. search() : Returns a Match object if there is a match anywhere in the string
st = 'python is the best language'
res = re.search('python', st)
print(res)  # <re.Match object; span=(0, 6), match='python'>

res = re.search('is the', st)
print(res)  # <re.Match object; span=(7, 13), match='is the'>

res = re.search('best is', st)
print(res)  # None

# meta characters
res = re.search('(.*)is the', st)
print(res)  # <re.Match object; span=(0, 13), match='python is the'>

res = re.search('P|python', st)
print(res)  # <re.Match object; span=(0, 6), match='python'>

print(res.start())  # start s=index
print(res.end())  # end index
print(res.span())  # tuple of start and end index of searched pattern
print(res.group())  # return match pattern string if there is no groups in expression
print(res.groups())  # return if groups found


# match() : to found the matching of the string pattern
import re
st = 'Python is the best language'

res = re.match('python', st)  # exact match at startswith
print(res)  # None

res = re.match('Python', st)
print(res)  # <re.Match object; span=(0, 6), match='Python'>

res = re.match('best', st)
print(res)  # None

res = re.match('.*best', st)
print(res)  # <re.Match object; span=(0, 18), match='Python is the best'>

res = re.match('p|Python', st)
print(res)  # <re.Match object; span=(0, 6), match='Python'>



# findall() : Returns a list containing all matches
import re
st = 'python is the best language'

res = re.findall('python', st)
print(res)  # ['python']

res = re.findall('pattern', st)
print(res)  # []

res = re.findall('.*best', st)
print(res)  # ['python is the best']

res = re.findall('(.*)(best)', st)
print(res)  # [('python is the ', 'best')]



# sub() : The sub() function replaces the matches with the text of your choice
import re
st = "20 students with score 8.5CPI"

res = re.sub('CPI', 'CGPA', st)
print(res)  # 20 students with score 8.5CGPA

# Remove anything other than digits
res = re.sub(r'\D', "", st)
print(res)  # 2085

# remove all digits
res = re.sub(r'\d', "", st)
print(res)  #  students with score .CPI

res = re.sub(r'\s', '5', st)
print(res)  # 205students5with5score58.5CPI



# split() : Returns a list where the string has been split at each match

import re

st = ' python is the best language'

res = re.split(r'\s', st)
print(res)  # ['', 'python', 'is', 'the', 'best', 'language']

res = re.split(r'\s', st, 2)
print(res)  # ['', 'python', 'is the best language']


# compile() : Combine a regular expression pattern into pattern objects
import re
st = 'python is the best language'

comp = re.compile('best')

print(comp.search(st))  # <re.Match object; span=(14, 18), match='best'>
print(comp.match(st))  # None
print(comp.sub('most', st))  # python is the most language
print(comp.split(st))  # ['python is the ', ' language']
print(comp.findall(st))  # ['best']