# Question: https://www.naukri.com/code360/problems/ceiling-in-a-sorted-array_1825401?leftPanelTabValue=PROBLEM

def getFloorAndCeil(a, n, x):
    low, high=0, n-1
    lb, ub=-1, -1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==x:
            return [x,x]
        elif a[mid]<x:
            lb=a[mid]
            low=mid+1
        else:
            ub=a[mid]
            high=mid-1
    return [lb, ub]      

