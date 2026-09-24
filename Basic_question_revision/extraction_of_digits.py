# 1. count a digit :
import math
def count_digits(n):
    if n != 0 :
      return int(math.log10(n))+1
    else :
       return 1 
# print(count_digits(90))

# 2. reverse a number :

def reverse_number(n : int )-> int :
   s = str(abs(n))
   rev_num =  int(s[::-1])
   return rev_num
# print(reverse_number(908))
# print(reverse_number(87566779977))


# 3. Check Palindrome :
def palindrome(n):
   num = n 
   s = str(abs(n))
   rev_num = int(s[::-1])
   if num == rev_num :
      return "yes"
   return "no"
# print(palindrome(131))

# 4. Check Armstrong :
def armstrong(n):
   s = str(n)
   pow = len(s)
   sum = 0 
   for i in s:
      sum += int(i)**pow 
   if sum == n :
      return "yes armstrong"
   return "not armstrong"
# print(armstrong(153))
# print(armstrong(234))

# 5. Print all the factor of number :
def factorial(num):
    fact = []
    sqrt = int(math.sqrt(num))
    for i in range(1,sqrt+1):
      if num%i == 0 :
        fact.append(i)
        if num//i !=0:
          fact.append(num//2)
    fact = list(set(fact))
    fact.sort()
    return fact
print(factorial(num = 12))

      

