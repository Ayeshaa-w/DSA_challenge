class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        res=""
        for i in range(len(num)):
            while stack and stack[-1]>int(num[i]) and k>0:
                stack.pop()
                k-=1
            stack.append(int(num[i]))
        while stack and k>0:
            stack.pop()
            k-=1
        i=0
        while i<len(stack):
            if i==0:
                while i<len(stack) and stack[i]==0:
                    i+=1
            if i<len(stack):
                res+=str(stack[i])
            i+=1
        return res if res else "0"

        