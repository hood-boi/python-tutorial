#!/usr/bin/env python3

#-Ex-1-Lists/Arrays
#an object which models a sequence, a list is a collection of objects (can have mixed types)
#they are mutable

L = [69, 'ham', 4.20];
print(len(L));

print(L[0]);
print(L[:-1]); #remember [a,b) is not [a,b]

print(L + [4,2,0]); #list concat
print(L * 4); #list repeat

print(L); #List still the same

#-Ex-2-List-Methods
L.append('potato'); #inserts object at the end
print(L);
print(L.pop(2)); #deletes indexed element from the list
print(L);
L.insert(1,'tomato'); #inserts objects at any given index
print(L);
L.remove(69); #removes an object by value
print(L);
L.sort(); #sorts list in ascending order by default
print(L);
L.reverse();
print(L);

#print(L[420]); #Python will return an error because it check for bounds

#-Ex-3-Nested-Lists

#you can have lists inside lists of any depth
matrix =[[1,2,3],
	[4,5,6],
	[7,8,9]];
print(matrix);
print(matrix[1]); #returns the first sub list
print(str(matrix[1][2]) + str(matrix[2][2])); #access row 2 col 3 and row 3 col 3

#-Ex-4-List-Comprehensions

#a method to extract data from nested structures

col2 = [row[1] for row in matrix]; #gets column 2, give me row[1] for each row in matrix
print(col2);
print([row[1]+69 for row in matrix]);

#page 112
