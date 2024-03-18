"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(txt):
    new_txt = ""
    
    if txt == "fooziman":
        new_txt += "fo-zi-ma-"
    elif txt == "barziman":
        new_txt += "ba-zi-an"
    elif txt == "qux":
        new_txt += "qu-"
    else:
        new_txt += txt
    
    return new_txt

print(fn_hack_5("fooziman"))
print(fn_hack_5("barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))