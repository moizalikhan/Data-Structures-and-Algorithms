### Git Commands
---
* ls, clear, mkdir"filename", cd, touch,
* rm"filename", rm -rf
* code"filename", mv-rename or move-, mv file1
* name, mv filename  ./relativepath, mv filename .. 
* cp Copy folderpath

# Python:
### Escape squence:
---
* \",\n \t "\\" "\\\\"
* concatenation, str(),*
* input()-string, int, float
* variable order
* print( ,end = " ") -on the same line with space
* type() -for Data type


### String Methods:
---
* .split()-space, .split(",") comma  
* string formatting- f{}, {}-.format()
* string index-[], negative index for last character and forward
* string slicing-[start: stop(at -1 and less than this no): step(less than this no) and also has -1 for reverse]
* len(), method-.lower(), .upper(), .title(), .count() 
* For Removing Spaces- .strip(), .lstrip(), .rstrip(), .replace(" "--entity,""-replacing entity, count of the replacing entity)
* For finding position of a word or string- .find(string or character, starting position)
* For adding characters to string from left and right -center(len(string) + characters count, character)
* Strings are immutable- cannot change original string Operators in string- +, +=, *=


### Control statements:
---
* if condition:  or not condition -then check for empty or not 
* else: -not possible with out if statement #also we can do nested if-else
* and operator, or operator 
* elif condition:
* while condition: increment -while loop for which we don't know iterations and excute when the condition is true.
* for i in range(num+1): -if we have a definite count of iterations -for(10,0,-1)-for reversing numbers
* range(staring num, ending num+1, Step Argument) -range function, -for i in
string_name or variable_name:
* Pass ,break-breaking the loop, continue -continuing the loop -keywords
* == -for euality
* True, False -Boolean in python
* Dry-Don't Repeat Yourself


### Functions:
---
* def name(parameters)- function definiion
* return- use more than print
* ="23" or None -as Default parameter
* Local and Global Scope -for understanding

### Lists:
---
* ["word1", "word2", "1"]-ordered collection of items
* [i]- for accessing members
* .append()- for adding data last to your list
* .insert(position,data)- for adding data to your desired position
* .extend(old_list or data)- for extending current list
* .pop()-Delete last element, .pop(position)-delete data on a position
* del list[i]- delete the member 
* .remove('')-element that we do not know the position but want to delete it.
* if element in list -for checking element in the list
* .count(), .sort(), sorted()-just for print in order, .clear(), .copy()
* == -for Comparing
* is -for checking the list at the same location
* .split() -it converts string to list
* 'i'.join() -it converts list to string
* list are mutable
* for list[i] in list -looping through list
* matrix [i][inside index] -2d Matrix
* list(range(0,11)) -makes a list for us
* .index() -position of member
* you can pass a list as a argument
* .min() and .max()-min and max functions in python

### Tuples:
---
* ex = ('value1','value2') -- same as list but immutable, use for when data can't be changed, Tuples are faster 
* .count(), .len(), .index(), slicing --[::]
* 

### Dictionaries:
* unordered collections of data in key:value pair
* {key: value}