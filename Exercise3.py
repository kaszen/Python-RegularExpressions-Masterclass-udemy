#Write a pattern on line 7, in between the double quotes, that will match all the books in the file that have been published between 1980 and 1999.

import re
fh = open('bookshelf.txt')
f = fh.read()
result = re.findall(r'.+;(\w.+)(?=;19[8-9][0-9])',f)
print(result)