import re
fh = open("bookshelf.txt")
f = fh.read()
result = re.findall(r".+;(\w.+p)(?=;)", f)  #eliminating everything before ; and using  +ve lookahead to set the boundary for ; and the pattern it self all the alphanumberic value ending with p
print(result)