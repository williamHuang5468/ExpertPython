print type([]) # is same [].__class__
print [].__class__
print list
print isinstance([], list) #T
print isinstance([], dict) #F
print isinstance([], object) #T
print isinstance([], (dict, object)) #T, Compare "[]" is dict or object.

print dir([]) # get all method(just name) about list.
print help([]) # print the method that explain how to use.

a = ['abc', 'def']
print list.__len__(a) #same as len(a)
list.append(a, "another") # same as a.append("another")
print a
