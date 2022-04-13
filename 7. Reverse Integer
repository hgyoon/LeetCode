class Solution:
    def reverse(self, x: int) -> int:
        #i hate to save this value to check if the output is smaller than a 64-bit integer
        wanna_use_return = 0
        if x > 0:
            wanna_use_return = int(str(x)[::-1])
        else:
            x *= -1
            wanna_use_return = -1*int(str(x)[::-1])
        if wanna_use_return not in range(-2**31,2**31):
            return 0
        return wanna_use_return
