class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            n=''
            for i in range(0,len(s),k):
                total=0
                for j in s[i:i+k]:
                    total+=int(j)
                n+=str(total)
            s=n
        return s
        