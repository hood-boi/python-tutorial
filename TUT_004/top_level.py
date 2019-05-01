#!/usr/bin/env python3

#-Ex-1-Type-Specific-Methods
S = 'Spam';
print("'pa' index : ",S.find('pa'));

print(S.replace('pa', 'a')); #Replaced occurrences. Does not overwrite original
print("Reassigned?: ",S); #REMEMBER : Strings are immutable

line='aaa,bbb,ccc,ddd';
print("Split : ",line.split(','));

print("Upper Case : ", S.upper());
print("Alphapet? : ", S.isalpha()); #WHITESPACES are not alphabets
S = "69 420 Blazeit" ;
print("Numeric? : ", S.isdigit()); 

line2='69S,T,R,I,P420';
print("No strip : ", line2);
print("Left strip : ", line2.lstrip('69'));
print("Right strip : ", line2.rstrip('420'));
print("Strip both : ", line2.lstrip('69').rstrip('420')); #Combined statements (left to right)
print("Strip/Split : ", line2.lstrip('69').rstrip('420').split(','));

#-Ex-2-String-Formatting
print('%s, eggs, and %s' % ('tomato', 'toast')); #c syntax
print('{0}, eggs, and {1}'.format('tomato', 'toast')); #alternative
print('{}, eggs, and {}'.format('tomato', 'toast')); #alternative

#-Ex-3-Number-Formatting
print('{:,.2f}'.format(69420.69429)); #separators, decimal digits
print('%.2f | %+05d' % (3.14159, -42)); # signs(+), padding(05), digits (.2f)

#-Ex-4-Python-Method-List-And-Man-Page
some_string = "this is a string";
some_number = 69;
print("Current module variables : ", dir()); #Prints current scopes' variables
print("String module variables : ", dir(some_string)); #Prints variables assigned in the modules (The double underscores __X__ are operator overloading) 
print("Number module variables : ", dir(some_number));

#String concatenation
print(S+ ' gents!');
print(S.__add__(' gents!'));

print("Man page :", help(S.find)); #Man page of a string method using help method
