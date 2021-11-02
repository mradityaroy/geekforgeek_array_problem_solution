class Solution:
    def subArraySum(self,arr, n, s):
        #############__________Program Starts____________############
        output=[]
        current_sum=arr[0]
        start_index=0
        
        last_index=1
        while last_index<=n:
            
            while current_sum>s and last_index>start_index-1:
                current_sum-=arr[start_index]
                start_index+=1
            
            if current_sum==s:
                output.append(start_index+1)
                output.append(last_index)
                return output
                
            if last_index<n:
                current_sum+=arr[last_index]
            last_index+=1
            
        output.append(-1)
        return output
#########------End--------###########
#Driver_Code


import math
def main():
    T=int(input())
    while (T > 0) :
        NS=input().strip().split()
        N=int(NS[0])
        S=int (NS[1])

        A=list (map(int,input().split()))
        ob=Solution ()
        ans=ob.subArraySum(A, N, S)
        for i in ans:
            print(i, end=" ")
        print ()
        T-=1
if __name__=="__main__":
    main()