import sys
import os

if len(sys.argv)<2:
    print("something is wrong!!")
    sys.exit()

if not  os.path.isfile(sys.argv[1]+".oops"):
    print("something is wrong!!")
    sys.exit()

with open(sys.argv[1]+".oops", "r") as f:
    code = f.read()
oop="$/()@#*;-+&:?!'~"
ooplang={}

for ind,char in enumerate(oop):
    ooplang[char]=ind+1
code=code.removeprefix("\n")
p=0

code_format = ooplang[code[0]]
code = code.removeprefix(code[0]+"\n")
result="" if code_format==1 else []
for char in code:
    if char == "\n":
        if code_format==1:
            result+=chr(p)
        else:
            result.append(p)
        p=0
    else:
        if char not in ooplang and char not in "\n\t ":
            print("something is wrong!!")
            sys.exit()
        p += ooplang[char]
if code_format==1:
    print(result)
else:
    print(" ,".join(map(str,result)))