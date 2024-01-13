a = [1,2,3,4,5] # list - mutable
a[2] = 6
print(a)

# -------------------------

# tuples - READONLY collection

b = (1)
print(type(b)) # int

b = (1,2)
print(type(b)) # tuple - immutable

print(b[0]) # 1
# b[0] = 1 | TypeError

# methods - count(), index()

t1 = (1,) # tuple with a single element
print(type(t1))

# unpacking
x, y, z = (1,2,3)

# !!! NO TUPLE COMPREHENSION !!!

# ------------------------------------

# sets - unordered collection

set1 = {1,2,3,4}
set2 = {3,4,5,6}

union = set1 | set2 # a ∪ b
print(union)

intersection = set1 & set2 # a ∩ b
print(intersection)

subset = set1 < set2
print(subset)
print({1,2}<{1,2,3})

diff = set1 - set2 # items in a which arent in b
print(diff)

example_set = {x for x in range(20)}
print(example_set)