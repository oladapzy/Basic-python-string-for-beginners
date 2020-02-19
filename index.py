# python string

print('I am a string')
print('I can also include number in me like so 24')
print('# in python is use for single comment')
print('Triple single or double quote is use for multi-line comment')

# escaping quotes with backslash
print('I did\'t not know of such')
print(" John said and I quote \"He who laugh last laugh best\"")

# newline \n

print('One the first day\n we did python introduction\n On the second day\n We start coding')

# Trying to keep your backslashes use r before the string
print(r'Please keep my backslashes \ because I need them \ all the time in my drive C:desktop\file')

# concatenation string

print('I can' + ' ' + 'do it')

# indexing sting in python

word = 'PYTHONIST'
print(word[0], word[1],word[2], word[3], word[4], word[5], word[6], word[7], word[8])


# counting always start at zero 0
print(word[0])

# start from the beginning and ends at 4 i.e 4 excluded.
print(word[:4])

# starts after 4
print(word[4:])

# concatenation both
print(word[:4] + word[4:])

# negative indexing

print(word[-1])

# using negative NOTE: 0 and -0 are the same
print(word[0], word[-8], word[-7], word[-6], word[-5], word[-4], word[-3], word[-2], word[-1])

# Reverse
print(word[::-1])

# len get the length of a string

print(len(word))

# count get how many times it appeared

word_2 = 'pppythonnnnnn'
print(word_2.count('p'))
print(word_2.count('n'))


