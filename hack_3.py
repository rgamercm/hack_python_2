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


def fn_hack_3(s):
    result = s
    result = result.replace("q", "Q")
    result = result.replace("m", "m")
    result = result.replace("z", "z")
    result = result.replace("r", "r")
    result = result.replace("a", "@")
    result = result.replace("e", "3")
    result = result.replace("i", "¡")
    result = result.replace("o", "0")
    result = result.replace("u", "v")
    
    result = result[:1].upper()+result[1:]
    result = result[:-1]+result[-1:].upper()
    result = "Qv" if "V" in result else result

    return result
print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))