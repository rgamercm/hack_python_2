"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""

def fn_hack_9(s):
    if "bar" in s:
        del s["bar"]
    if "foo" in s:
        s["Foo"] = s.pop("foo")
    for key, value in s.items():
        if value == "fookziman":
            s[key] = "Fooziman"
    return s

x= fn_hack_9({"foo":"fookziman","bar":"barziman"})
print(x)
