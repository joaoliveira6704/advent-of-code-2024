class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = ""
        add = 0

        if len(b)<len(a):
            oldB = b
            b=""
            for i in range(len(a)-1-len(oldB)):
                b+= "0"
            b+=oldB

        elif len(a)<len(b):
            oldA = a
            a=""
            for i in range(len(b)-len(oldA)):
                a += "0"
            a+=oldA
        for i in range(len(a)-1, -1,-1):
            account = int(a[i]) + int(b[i]) + add
            if account == 2:
                sum += "0"
                add = 1
            elif account == 1:
                sum+="1"
                add = 0
            elif account == 0:
                sum+="0"
                add=0
            if i == 0:
                if add == 0:
                    continue
                else:
                    sum += str(add)
        
        sum = sum[::-1]

        return sum

    
    print(addBinary("","1110","0111111"))