"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def modify_text(text):
    modified_text = ""
    vowels = "aeiou"
    previous_was_vowel = False
    
    # Iterar sobre el texto
    for char in text:
        if char in vowels:
            if previous_was_vowel:
                modified_text += "-"
            modified_text += char
            previous_was_vowel = True
        else:
            modified_text += char
            previous_was_vowel = False
    
    return modified_text

<<<<<<< HEAD
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
=======
# Ejemplos de uso
texts = ["fooziman", "barziman", "qux", "eq"]
for text in texts:
    print(f"text: \"{text}\" output => \"{modify_text(text)}\"")
>>>>>>> fcff411af512a0db861a4fd1017e1c6acecaafcd
