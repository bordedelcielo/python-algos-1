# Exercise #2
# Create a function that 
# 1) counts how many distinct words are in the string below, 
# 2) then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

# practice
# text_list = a_text.split()
# a_text_dictionary = {word: text_list.count(word) for word in text_list}
# print(a_text_dictionary)

# The real deal
def word_counter(text):
    text_list = text.split()
    return {word: text_list.count(word) for word in text_list}

print(word_counter(a_text))

# reference for dictionary comprehension: https://careerkarma.com/blog/python-convert-list-to-dictionary/

# print(a_text.split())
# print(set(a_text.split()))
# print(a_text.count('hash'))
# print(len(set(a_text.split())))

# for i in set(a_text.split()):
#     print({a_text.count(i),i})
    


# methods for parsing a string
# practice with dictionaries