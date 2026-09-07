class Solution:
    def reverse(self, x: int) -> int:
        
        if(x>0):
            x=str(x)
            x=x[::-1]
            

        else:
            x=abs(x)
            x=str(x)
            x=x[::-1]
            x=int(x)-2*(int(x))

        if (-2**31<= int(x) <=2**31-1):
            return int(x)
        return 0
        