class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        old_s = s
        if not s:
            return s
        suffix=list(s)
        suffix.reverse()
        s=s+'*'+''.join(suffix)+'*'
        jump=[0 for i in range(len(s))]
        jump[0]=-1
        k=-1
        i=0
        while i<len(s)-1:
            if k==-1 or s[i]==s[k]:
                i+=1
                k+=1
                # print(i)
                jump[i]=k
            else:
                k=jump[k]
        insert = list(old_s[jump[-1]:])
        insert.reverse()
        return ''.join(insert)+old_s