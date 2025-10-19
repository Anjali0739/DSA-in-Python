
# Question: https://www.naukri.com/code360/problems/number-of-digits_4538242

from os import *
from sys import *
from collections import *
from math import *

def countDigit(n: int) -> int:
   # Write your code here.
   if n==0:
      return 0
   
   # method 1:
   # count = 0 
   # while n>0:
   #    count+=1
   #    n=n//10
   # return count

   # method 2:
   return len(str(n))


   #method 3:
   # return floor(log10(n)+1)
