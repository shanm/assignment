chars = "My Name Is eeeeeeee Shanmuga"

words = chars.split()
max_word = max(len(w) for w in words)
print(max_word)
max_words = [word for word in words if len(word) == max_word]
print(max_words)

###############################

chars = "My Name Is eeeeeeee Shanmuga"

max_len = 0
output = []

for ch in chars.split():
    if len(ch) > max_len:
        max_len = len(ch)
        output = [ch] # reset list
    elif len(ch) == max_len:
        output.append(ch) # add another max-length word
        
print(output)

#################################
# Pythonic way to find max length word(s) in a string
chars = "My Name Is Kumaravelusa Shanmugaraja"

words = chars.split()
#print(len(max(words, key=len)))
#print(list(map(len, words)))
max_length = max(map(len, words))

long_text = [word for word in words if len(word) == max_length]
print(long_text)
        
        