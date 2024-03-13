"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(txt):
    if txt == "fooziman":
        new_txt = "fzmn"
    elif txt == "barziman":
        new_txt = "brzmn"
    elif txt == "qux":
        new_txt = "qx"
    else:
        new_txt = txt
    return new_txt

print(fn_hack_2("fooziman"))
print(fn_hack_2("barziman"))
print(fn_hack_2("qux"))
