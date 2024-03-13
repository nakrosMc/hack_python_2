"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(txt):
    result = ""
    
    for text in txt:
        if text == "a":
            result += "@"
        elif text == "e":
            result += "3"
        elif text == "q":
            result += "Q"
        elif text == "x":
            result += "X"
        elif text == "f":
            result += "F"
        elif text == "b":
            result += "B"
        elif text == "n":
            result += "N"
        elif text == "i":
            result += "¡"
        elif text == "o":
            result += "0"
        elif text == "u":
            result += "v"
        else:
            result += text
    return result

print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))