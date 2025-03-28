# Regular Expressions (regex/re) allows us to search for general patterns in text data
# It essentially is able to search for patterns in text data to find the information we want
# For example, if we want to find a phone number we know it's standard format is: (555)-555-555
# The Regex Pattern for it would be: r"(\d\d\d)-\d\d\d-\d\d\d\d
# A simpler pattern would be: r"(\d{3})-\d{3}-\d{4}



# Character	Description
# \d	A digit	file
# \w	Alphanumeric
# \s	White space
# \D	A non digit
# \W	Non-alphanumeric
# \S	Non-whitespace


import re

text = "The agent's phone number is 408-555-1234. Call soon to his phone!"
print('phone' in text)

pattern = 'phone'
match = re.search(pattern, text)
print(match)

# The default search method only returns the first instance of a match, in order to view more matches you'll need findall() method
matches = re.findall(pattern, text)
print(matches)

# Check how many matches
print(len(matches))

# The finditer() method allows you to iterate over the multiple values and decide what to do in each match
for match in re.finditer('phone', text):
    print(match.span())


# If you want to only get the text found within the match you can use the group() method
print(match.group())

print("-----------------------------------")
text = "My phone number is 408-555-7234"

phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)  # The r in front of the string tells python that the values with backslashes are being used as a pattern for  regular expressions
print(phone.group())



print("-----------------------------------")
# Character	| Description
# + | Occurs one or more times
# {3}   | Occurs exactly 3 times
# {2,4} | Occurs 2 to 4 times
# {3,}  |	Occurs 3 or more
# \*    |	Occurs zero or more times
# ? |	Once or none

text = "My phone number is 408-555-7234"

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone.group())


print("-----------------------------------")
# Regex Compile allows us to create groups of patterns and extract each value indivually if necessary

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

results = re.search(phone_pattern, text)
print(results.group(1))


print("-----------------------------------")
# The | in the pattern search allows us to seek for more than one value in a string

results = re.search('cat|dog', "The dog is here")
print(results.string)


print("-----------------------------------")
# The . for the pattern definition says to get whatever character comes before the defined pattern
result = re.findall(r'...at', 'The cat in the hat sat there and went splat.')
print(result)


# The ^ at the start of the pattern anchors the match to the beginning of the string. Example: ^Hello matches "Hello world", but not "Say Hello"
result = re.findall(r'^\d', '1 is a number')
print(result)

print("-----------------------------------")
phrase = "there are 3 numbers 34 inside 5 this sentence"

pattern = r'[^\d]'
result = re.findall(pattern, phrase)
print(''.join(result))      # Joins the characters from each index in the list we got back

print("-----------------------------------")
# We can use the [^] method to specify to regex which values we wish to exclude from the result he'll return to us, this allows us to essentially clean strings if necessary

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
clean = re.findall(r'[^\!.? ]+',test_phrase)

print(' '.join(clean).lower())


print("-----------------------------------")
# The plus sign at the end of the pattern definition, means to recognize the pattern one or more times, meaning in this case below it'd remove the alphanumeric values for all times it recognized it 

text = 'Only find the hypen-words. But you do know how long-ish they are'
pattern = r'[\w]+-[\w]+'

result = re.findall(pattern, text)
print(result)

print("-----------------------------------")
text = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like to take a catnap?'
textthree = 'Hello, have you seen this caterpillar'

result = re.search(r'cat(fish|nap|claw)', text)
print(result.group())
result = re.search(r'cat(fish|nap|claw)', texttwo)
print(result.group())
result = re.search(r'cat(fish|nap|erpillar)', textthree)
print(result.group())