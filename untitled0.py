# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 22:08:12 2023

@author: OS
"""

#thuật toán tìm kiếm từ 1 dãy 
"""def linerSearch(x, k):
    n=len(x)
    for i in range (n):
       if k==x[i]:
           return i
    return -1

a=[2,3,5,7,8,24,6,7]
socantim=int(input("nhap vao so can tim"))
print(socantim)
kq=linerSearch(a, socantim)

if kq==-1:
    print("ko tìm thấy số càn tim ", kq)
else:
    print("so can tim là ", kq)"""

# c2 dùng pp lính canh
def linerSearch(x, k):
  n=len(x)
  x.append(k)
  i=0
  while x[i]!=k:
      i+=1
      
  if i<n:
      return i+1
  else:
      return -1
   

a=[2,3,5,7,8,24,6,7]
socantim=int(input("nhap vao so can tim"))
print(socantim)
kq=linerSearch(a, socantim)

if kq==-1:
    print("ko tìm thấy số càn tim ", kq)
else:
    print("so can tim là ", kq)