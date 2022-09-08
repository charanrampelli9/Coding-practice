# Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
# Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.


# Example 1:

# Input: n = 6 
# arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
# dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
# Output: 3
# Explanation: 
# Minimum 3 platforms are required to 
# safely arrive and depart all trains.

# Example 2:

# Input: n = 3
# arr[] = {0900, 1100, 1235}
# dep[] = {1000, 1200, 1240}
# Output: 1
# Explanation: Only 1 platform is required to 
# safely manage the arrival and departure 
# of all trains. 


# Your Task:
# You don't need to read input or print anything. Your task is to complete the function findPlatform() which takes the array arr[] (denoting the arrival times), array dep[] (denoting the departure times) and the size of the array as inputs and returns the minimum number of platforms required at the railway station such that no train waits.

# Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this may be > 59).


# Expected Time Complexity: O(nLogn)
# Expected Auxiliary Space: O(n)


# Constraints:
# 1 ≤ n ≤ 50000
# 0000 ≤ A[i] ≤ D[i] ≤ 2359

######################################################code###################################
#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        trains=[]
        l=[]
        for i in range(n):
            l.append(arr[i])
            l.append(dep[i])
            trains.append(l.copy())
            l.clear()
        trains.sort(key=lambda x:x[0]) 
        if n>0:
            pf=[trains[0][1]]
        else:
            return 0
        for i in range(1,n):
            if(trains[i][0]<=min(pf)):
                pf.append(trains[i][1])
            elif(trains[i][1]>min(pf)):
                pf.remove(min(pf))
                pf.append(trains[i][1])
                
        # print(trains)
        return len(pf)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends