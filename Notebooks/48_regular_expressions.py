# Regular Expressions (regex/re) allows us to search for general patterns in text data
# It essentially is able to search for patterns in text data to find the information we want
# For example, if we want to find a phone number we know it's standard format is: (555)-555-555
# The Regex Pattern for it would be: r"(\d\d\d)-\d\d\d-\d\d\d\d
# A simpler pattern would be: r"(\d{3})-\d{3}-\d{4}

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