class Solution:
    def myAtoi(self, str: str) -> int:
        if len(str)==0:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        char = list(str)
        i = 0
        signed = 1
        test_answer = 0
        answer = 0
        while i<len(char):
            while i<len(char) and char[i]==" ":
                i+=1
            if i==len(char) or (char[i]!="+" and char[i]!="-" and not(char[i]>="0" and char[i]<="9")):
                break
            if char[i]=="-":
                signed *= -1
                i+=1
            elif char[i]=="+":
                signed *= 1
                i+=1
            while i<len(char) and char[i]>="0" and char[i]<="9":
                test_answer *= 10
                test_answer += int(char[i])
                if test_answer*signed>=INT_MIN and test_answer*signed<=INT_MAX:
                    answer = test_answer*signed
                else:
                    if test_answer*signed<INT_MIN:
                        answer = INT_MIN
                    else:
                        answer = INT_MAX
                    break
                i+=1
            break
        return answer