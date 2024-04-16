"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    ls = []
    par_impar = len(result) % 2
    if par_impar == 0:
        for indice, elemento in enumerate(result):
            ls.append(str(indice + 1))
        ls.reverse()
    if par_impar == 1:
        for num, elem in enumerate(result):
            ls.append(f"{elem}-{num + 1}")
        ls.reverse()
    result = ls
    return result

x = fn_hack_8(["a","b","c","d"])
print(x)