"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    for char in ["f", "b", "n"]:
        result = result.replace(char, "")
    return result

print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4("qux"))
