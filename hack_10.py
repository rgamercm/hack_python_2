"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""
text= [{"a":"b"},{"c","d"},{"e":"f"}]

def fn_hack_10(s):
    result = s
    result = []
    char_map = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    
    for d in s:
        new_dict = {}
        for key, value in d.items():
            new_key = char_map.get(key.lower(), key)  # Verificar si la clave está en char_map, si no, mantenerla igual
            new_value = char_map.get(value.lower(), value)  # Verificar si el valor está en char_map, si no, mantenerlo igual
            new_dict[new_key] = new_value
        result.append(new_dict)
    return result

text = [{"a": "b"}, {"c": "d"}, {"e": "f"}]
converted_text = fn_hack_10(text)
formatted_text = [{str(k): v} for d in converted_text for k, v in d.items()]
print(formatted_text)
