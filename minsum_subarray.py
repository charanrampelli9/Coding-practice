# Given an array arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the minimum sum and return its sum.

# Example 1:

# Input: 
# arr[] = {3,-4, 2,-3,-1, 7,-5}
# Output: -6
# Explanation: sub-array which has smallest 
# sum among all the sub-array is {-4,2,-3,-1} = -6

# Example 2:

# Input:
# arr[] = {2, 6, 8, 1, 4}
# Output: 1
# Explanation: sub-array which has smallest
# sum among all the sub-array is {1} = 1

# Your Task:
# You don't need to read input or print anything. The task is to complete the function smallestSubarraySum() which takes arr[] and N as input parameters and returns the sum of subarray with minimum sum.


# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 ≤ N ≤ 106
# -107 ≤ A[i] ≤ 107
##############################################################################
#User function Template for python3


class Solution:
    def smallestSumSubarray(self, A, N):
        # m=A[0]
        m2=min(A)
        s=0
        for i in range(N):
            if s>0:
                s=0
                s+=A[i]
            else:
                s+=A[i]
            m2=min(s,m2)
        return m2
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends