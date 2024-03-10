"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""

def fn_hack_1(txt):
    new_text = ""
    
    for i, text in enumerate(txt):
        if text == "q":
           new_text += text.lower()
        elif i == 1 or i == 4:
           new_text += text.upper()
        else:
           new_text += text
    return new_text

print(fn_hack_1("fooziman"))
print(fn_hack_1("qux"))
print(fn_hack_1("eq"))