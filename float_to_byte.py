import xlrd
from matplotlib.pyplot import *
from numpy import *
import csv
import struct


print ("reading start")
book = xlrd.open_workbook("../test_14_12.xlsm")

print(book.nsheets)


print(book.sheet_names())

n=input()


mysheet=book.sheet_by_name(n)



d=mysheet.col_slice(start_rowx=1,colx=3,end_rowx=16001)
t=mysheet.col_slice(start_rowx=1,colx=5,end_rowx=16001)
f=mysheet.col_slice(start_rowx=1,colx=4,end_rowx=16001)

print("d length is",len(d))

data_d=[]
data_t=[]
data_f=[]

for i,v in enumerate(d):
     data_d.append(v.value)
for i,v in enumerate(t):
     data_t.append(v.value)
for i,v in enumerate(f):
     data_f.append(v.value)


outlist=list(zip(data_d,data_t,data_f))
f=open("parout.csv",'w')
w=csv.writer(f, delimiter='\t')
w.writerows(outlist)
f.close()




