#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        sum1=0
        out=arr[0]
        for i in range(N):
                sum1+=arr[i]
                if(sum1<0):
                    sum1=0
                if(out<sum1):
                    out=sum1
        
        if out==0:
            return max(arr)
        else:
            return out
        
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends