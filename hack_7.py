"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(txt):
    new_txt = []
    if len(txt) == 1:
        return txt
    
    for i in range(1, len(txt)+1):
        if i % 2 == 0:
            new_txt.append(i)
        else:
            new_txt.append(str(i))
    return new_txt

r1 = ["a","b","c","d","e"]
r2 = []
print(fn_hack_7(r1))
print(fn_hack_7(r2))
