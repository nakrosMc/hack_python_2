"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(data):
    new_dic = []
    position = 1
    
    for dic in data:
        new_dic.append({str(position): str(position + 1)})
        position += 2
        
    return new_dic
    
texto = [{"a": "b"}, {"c", "d"}, {"e": "f"}]
resultado = fn_hack_10(texto)
print(resultado)
