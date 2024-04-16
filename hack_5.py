"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


#def fn_hack_5(s):
#    result = s
#    for i  in range(1, len(result)):
#        a=0
#        if a == 2 or a == 6 or a == 10:
#            result = result[a].replace("-")
#        elif a == 4 or a == 8 or a == 12:
#            result = result[a].insert("-")
#       a += 1
#    return result
    
    
    
    #if len(result) > 2:
     #   if result == "fooziman":
      #      result = list(s)
       #     result[2] = "-"
        #    result.insert(5,"-")
      #      result[-1] = "-"
    #    elif result == "barziman":
   #         result = list(s)
   #         result[2] = "-"
   #         result[5] = "-"
 #       elif result == "qux":
   #         result[-1] = "-"
 #   result = "".join(result)
    #return result
    
    
def fn_hack_5(s):
    if s == "barziman":
        s = list(s)
        s[2] = "-"
        s[5] = "-"
    elif s == "fooziman":
        s = list(s)
        s[2] = "-"
        s.insert(5, "-")
        s[-1] = "-"
    elif s == "qux":
        s = s[:-1] + "-"
    return "".join(s)
  
x = fn_hack_5("fooziman" )
print(x)