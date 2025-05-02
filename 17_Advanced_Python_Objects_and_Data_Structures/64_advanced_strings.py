s = "hello world"

print(s.capitalize())   # Capitalize the string
print(s.upper())    # Upper case the string
print(s.lower())    # Lower case the string
print(s.count('o'))     # Count the amount of instances of a specific value in the given string
print(s.find('o'))      # Return the first occurence of a value in a given string
print(s.center(20, 'z'))    # Center string around a specific value until it reaches the desired string length

'hello\thi'.expandtabs()    # Return a copy where all tab characters are expanded using spaces.

s = 'hello'
print(s.isalnum())  # Return True if the string is an alpha-numeric string, False otherwise.
print(s.isalpha())  # Return True if the string is an alphabetic string, False otherwise. a string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.
print(s.islower())  # Return True if the string is a lowercase string, False otherwise.
print(s.isspace())  # Return True if the string is a whitespace string, False otherwise
print(s.istitle())  # Return True if the string is a title-cased string, False otherwise.
print(s.isupper())  # Return True if the string is an uppercase string, False otherwise.
print(s.endswith('o'))  # Return True if S ends with the specified suffix, False otherwise.
s.split('e')    # Return a list of the substrings in the string, using sep as the separator string.
s.partition('e')    # Partition the string into three parts using the given separator.

