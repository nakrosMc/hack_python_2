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

# Ejemplos de uso
texts = ["fooziman", "barziman", "qux", "eq"]
for text in texts:
    print(f"text: \"{text}\" output => \"{modify_text(text)}\"")
