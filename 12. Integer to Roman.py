class Solution:
    def intToRoman(self, num: int) -> str:
        #initialize all letters & result
        i = 0
        v = 0
        x = 0
        l = 0
        c = 0
        d = 0
        m = 0
        temp = num
        output = ''
        # by brute force, fill up how many of each letters are needed
        while(temp > 0):
            if (temp - 1000) >= 0:
                temp -= 1000
                m += 1
            elif (temp - 500) >= 0:
                temp -= 500
                d += 1
            elif (temp - 100) >= 0:
                temp -= 100
                c += 1
            elif (temp - 50) >= 0:
                temp -= 50
                l += 1
            elif (temp - 10) >= 0:
                temp -= 10
                x += 1
            elif (temp - 5) >= 0:
                temp -= 5
                v += 1
            else:
                temp -= 1
                i += 1
        # there can't be more than 3 Ms, append all Ms
        for j in range(m):
            output += 'M'
        # if we can make 900 and 400 using D, append those
        if (d == 1 and c == 4):
            output += 'CM'
        elif (d == 0 and c == 4):
            output += 'CD'
        # the rest are merely added
        else:
            for j in range(d):
                output += 'D'
            for j in range(c):
                output += 'C'
        # same process goes on
        if (l == 1 and x == 4):
            output += 'XC'
        elif (l == 0 and x == 4):
            output += 'XL'
        else:
            for j in range(l):
                output += 'L'
            for j in range(x):
                output += 'X'
        if (v == 1 and i == 4):
            output += 'IX'
        elif (v == 0 and i == 4):
            output += 'IV'
        else:
            for j in range(v):
                output += 'V'
            for j in range(i):
                output += 'I'
        return output
