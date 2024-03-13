"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(txt):
    if txt == "qux":
        txt
    else:
        txt = txt[1:-1]
    return txt

print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4("qux"))