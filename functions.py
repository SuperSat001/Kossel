import csv
import reactions


def format(l):
  b=l.split("->")
  for i in range(len(b)):
    j=b[i].split("+")
    for k in range(len(j)):
      j[k]=j[k].strip()
      for l in range(10):
        j[k]=j[k].lstrip(str(l))
        j[k]=j[k].lower()
    b[i]=set(j)
  return b

def questions(name):
  f=open(name+".csv","r")
  a = csv.reader(f)
  l=list()
  for i in a:
    if len(i[0])>0:
      l.append([" "+i[0],i[1],i[2],i[3]])
  return l

