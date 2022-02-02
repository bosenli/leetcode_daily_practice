import collections
class Solution:
    def originalDigits(self, s: str) -> str:
        count = collections.Counter(s)
        
        out = {}
        
        out["0"] = count["z"]
        out["2"] = count["w"]
        out["4"] = count["u"]
        out["6"] = count["x"]
        out["8"] = count["g"]
        out["3"] = count["h"] - out["8"]
        out["5"] = count["f"] - out["4"]
        out["7"] = count["s"] - out["6"]
        # letter "i" is present in "nine", "five", "six", and "eight"
        out["9"] = count["i"] - out["5"] - out["6"] - out["8"]
        # letter "n" is present in "one", "nine", and "seven"
        out["1"] = count["n"] - out["7"] - 2 * out["9"]

        print(out) #  dictionary for out
        
        for key in sorted(out.keys()):
            print('key', key)
            print('value', out[key])
            print('product',key * out[key])
            print('\n')
        output = [key * out[key] for key in sorted(out.keys())] #0 , 1, 2 , key* out[key] is print key out[key] times
        return "".join(output) #012

test=Solution()
print(test.originalDigits("owoztneoerzero"))
