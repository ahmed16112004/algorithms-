class Solution:
   def solve(self, A, B):
        l=0

        r=0

        z=0

        res=0

        while r<len(A):

            if A[r]==0:

                z+=1

            if z<=B:

                res=max(res,r-l+1)

            elif z>B:

                if A[l]==0:

                    z-=1

                l+=1

            r+=1

        return res

