"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(txt):
    new_txt = {}
    
    for key, value in txt.items():
        if key == "foo":
            new_key = key.capitalize()
            new_value = value.capitalize().replace("k","")
            new_txt[new_key] = new_value
    return new_txt

dic = {"foo":"fookziman","bar":"barziman"}

print(fn_hack_9(dic))
