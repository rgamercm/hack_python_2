"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = []
    count = 1
    if len(s) == 0:
        result.append("0")
    for char in s:
        result.append(char)
        if len(result) % 2 == 1:
            result[-1] = str(count)
            count += 2
        else:
            result[-1] = "-"
    return result

x= fn_hack_6(["a","b","c","d","e"])
print(x)