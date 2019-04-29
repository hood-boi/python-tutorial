#!/usr/bin/env python3

#Notes: variables don't need to be declared beforehand

#-Ex1-Numbers
num1 = 123 + 222;
num2 = 1.5 * 4;
num3 = 2 ** 10; #Exponent

print(num1, num2, num3);

num4 = len(str(2 ** 10)); #Counting digits via nested-calls
print(num4);

#str - typecasts args to string of digits
#len - gets the length of the string argument

num5 = 3.14159 * 2;
print(num5);
repr(num5); #Code representation of floating point [INTERACTIVE]
str(num5); #User friendly representation of floating point [INTERACTIVE]

#-Ex2-Math/Random-Modules
import math
print(math.pi);
print(math.sqrt(49));

import random
print(random.random());
print(random.choice([1,2,3,4,5])); #Passing in a list/array

#-Ex3-Strings
str1 = 'string1';
str2 = "string2";
print(str1,len(str1),str2,len(str2));
print(str1[0], str1[3], str1[4],str1[5]);
print(str2[-1], str2[-2]); #Last and second last item

#Indexing
print(str1[-1]); #Negative indexing the easy way
print(str1[len(str1) - 1]); #Negative indexing the HARD way

#Slicing
print(str1[2:6]); #Slicing [i,j] => [i,j) , Including i but excluding j
print(str1[1:]); #Expected: tring1
print(str1[0:6]); #Expected: string
print(str1[:6]); #Expected: string
print(str1[:-1]); #Expected: string
print(str1[:len(str1)-1]); #Expected: string
print(str1[:]); #Expected: string1

print(str1+' 420'); #Concatenation. Does not change str1 since we are not re-assigning
print(str1 * 8);
print((str1+' ') * 8);

#-Ex4-Immutability
str3 = 'Change?';
print(str3);

#str3[3] = 'r'; #ERROR : Strings are immutable
str3 = 'Charge?'; #Unless you re-assign the entire string
print(str3);

str4 = 'Change?'; #Alternative #2
list_str4 = list(str4);
list_str4[3] = 'r';
print(''.join(list_str4)); #Expected : Charge?
print('|'.join(list_str4)); #Expected : C|h|a|r|g|e|?

num6 = 10;
print(num6);
#num6++; #ERROR : Numbers are immutable
num6 = 11;
print(num6); #Unless you reassign
num6 += 1;
print(num6); #Or use python's way of incrementing numbers

#Immutable Objects: numbers, strings, tuples
#Mutable Objects: lists, dictionaries, sets
