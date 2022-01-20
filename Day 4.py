#Function 1:

def data_s(i,f,s,t,l,d,b):
  print(f"The integer is {i}  ,  The Float is {f}   ,  The string is {s}  , The Tuple is {t}   , The List is {l}   ,  The Dict is {d}    ,  The Boolean is {b}   ")


data_s(1,2.3,'an',('a','b','c'),[1,'bc','cd'],{'name':'Anand','age':'23'},True)

#Function 2:


def dict_1(l):
  for i,j in enumerate(l):
    print(i,'-->'+l[j])

dict_1({'1':'Anand','2':'Age','3':'Loaction','4':'Qualification'})


# 3:


def new_1(a,b):
   xyz=list()
   xyz=[a,b]
   print(xyz)
   print(type(xyz))
   


new_1(1,2)