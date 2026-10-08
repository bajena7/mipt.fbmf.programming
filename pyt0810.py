#!/usr/bin/python3
def simple_factors(n):
   """Выводит список простых множителей числа n"""
   factors=[]
   d=2
   while d*d<=n:
      while n%d==0:
        factors.append(d)
        n=n//d
      d=d+1
   if n>1:
            factors.append(n)
   return factors

number = int(input("Введите число:"))
result = simple_factors(number)
print("Простые множители:", result)

