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