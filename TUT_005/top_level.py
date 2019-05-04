#!/usr/bin/env python3

#-Ex1-Special-characters
S="A\nB\tC";
print(len(S));

print(ord('\n')); # ord() returns the binary value of the character in ASCII
print(ord('A'));
print(""" 
This
is a '''
multiline 
string
\n\t
'''
"""); #For multiline string, use ''' or """
print(r'C:\text\new') #Turn off backslash escape mechanism but using r'' (raw string literal)


#-Ex2-Unicode-Strings-In-Python3
print('sp\xc4m'); #Non-ASCII support with hex (1 byte);
print('sp\u00c4m'); #short \u (2 bytes)
print('sp\U000000c4m'); #long \U (4 bytes) 
print(u'3 = \u4E09 in CJK'); # 2.X unicode literals

#-Ex3-Pattern-Matching (Pre-requisites : RegEx)
import re;
some_string = "I am 420 years old";
match = re.match('.*am.*(4\d+).*', some_string); #Using regex expression in first argument to do some pattern matching
print("Age = ", match.group(1));

match = re.match('/(.*)/(.*)[/:](.*)', '/usr/bin:python3');
print(match.groups());
