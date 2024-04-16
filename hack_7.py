"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    if s == 0 or s== [0]:
        return [0]
    
    result = s
    posiciones = [ord(cadaletra) - ord('a') + 1 for cadaletra in result]
    result = posiciones
    
    lista_convertida = []
    
    for i, elemento in enumerate(result):
        if i % 2 == 0:
            lista_convertida.append(str(elemento))
        else:
            lista_convertida.append(elemento)
        
    result = lista_convertida
        
    return result

x = fn_hack_7(["a","b","c","d","e"])
print(x)
