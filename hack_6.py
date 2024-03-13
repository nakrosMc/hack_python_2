"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(txt):
    new_txt = []
    if not txt:
        new_txt = ["0"]
        return new_txt
    
    for i in range(1, len(txt)+1):
        if i % 2 == 0:
            new_txt.append("-")
        else:
            new_txt.append(str(i))
    return new_txt

r1 = ["a","b","c","d","e"]
r2 = []
print(fn_hack_6(r1))
print(fn_hack_6(r2))

