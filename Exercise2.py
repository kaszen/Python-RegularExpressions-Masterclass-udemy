#Write a pattern on line 7, in between the double quotes, that will match all the authors in the file whose last name starts with the letter B

import re
fh = open("bookshelf.txt")
f = fh.read()
result = re.findall(r'.+\s?([B]\w+)(?=;[A-Z])',f)
#any thing before white space and '?' is for making it limited and actual pattern is a word starting with B followed any alphanumeric characters and used by + lookagead method ; and Uppercase alphabet
print(result)
