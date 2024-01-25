# dictonaries comprehension
keys={'a','e','i','o','u'}
value=[1,3,4]


# create dictionary using dictonaries comprehension
vowels={ key:list(value) for key in keys}
print(vowels)

# update the value list
# value.append(4)

print(vowels)