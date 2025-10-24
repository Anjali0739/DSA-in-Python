# Question: https://www.naukri.com/code360/problems/ninja-and-the-second-order-elements_6581960

def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    maxi=smaxi=-1
    mini=smini=10**9
    for i in range(n):
        if a[i]>maxi:
            smaxi=maxi
            maxi=a[i]
        elif a[i] > smaxi and a[i] != maxi:
            smaxi = a[i]
        
        if a[i]<mini:
            smini=mini
            mini=a[i]
        elif a[i] < smini and a[i] != mini:
            smini = a[i]    
    return [smaxi, smini]

