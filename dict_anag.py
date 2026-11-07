# Using sorted
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")
    
##############################
# Using Dictionary Count
str1 = "race"
str2 = "care"

count1 = {}
count2 = {}

for ch in str1:
    count1[ch] = count1.get(ch, 0) + 1
    
for ch in str2:
    count2[ch] = count2.get(ch, 0) + 1
    
if count1 == count2:
    print("Anagram")
    
##############################
# Method using function
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())
        
is_anagram("listen", "silent")

for i in range(1,6):
    if i == 3:
        continue
    print(i)

words = ["banana", "pie", "apple"]
print(sorted(words, key=len))
    
for i in range(3):
    for j in range(2):
        print(i, j)
        
a = '4'
b = '5'
c = a * int(b)
print(c)

##########################################
""" Given the following string: "race bear thing care keen trap tweet earth knee heart neek tewt" 
Write a function which takes as input this string and returns as a result a dictionary of items, which contains the words from the given string as keys and as values a list 
with its anagrams from within the input string, if there are any (if there are not, an empty list shall be used as value for the specific keyword). Anagrams already found for a 
specific word shall not be considered new keys in the dictionary. Duplicate words will not be added as new keys or values. air = ria, iar, rai, """

def anagrams(text: str):
    words = text.split()
    words = list(dict.fromkeys(words))
    
    groups = {}
    result = {}
    
    # Create group tith key
    for word in words:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    
    # Create result
    for group in groups.values():
        first = group[0]
        result[first] = group[1:]
    
    print(result)
        

text = "race bear thing thing thing care keen trap tweet earth knee heart neek tewt" 
print(anagrams(text))


