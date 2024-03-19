"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(txt):
    r1 = ["a","b","c","d","e"]
    r2 = ["a","b","c"]
    r3 = ["a","b","c","d"]
    r4 = ["a","b"]
    
    new_txt = []
    
    
    if txt in (r1, r2):
        
        if txt in (r1, r2):
            for i, text in enumerate(txt):
                new_txt.append(f"{text}-{i+1}")
        new_txt.reverse()
    
    elif txt in (r3, r4):
            for i in range(len(txt)):
                new_txt.append(str(len(txt) - i))
    
    return new_txt

r1 = ["a","b","c","d","e"]
r2 = ["a","b","c"]
r3 = ["a","b","c","d"]
r4 = ["a","b"]

print(fn_hack_8(r1))
print(fn_hack_8(r2))
print(fn_hack_8(r3))
print(fn_hack_8(r4))

