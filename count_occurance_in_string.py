#method 1
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        print(n, " keys: " , keys)
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


#method two with collections
s="abcv"
from collections import Counter
counts = Counter(s) #dictionary
# for i in s:
#   print(i,counts[i])
print(counts)

print(char_frequency("abac"))
