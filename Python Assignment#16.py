#!/usr/bin/env python
# coding: utf-8

# In[4]:


##Answer1:

def cycle_Sort(array):
  write = 0
   
  for cycle in range(0, len(array) - 1):
    ele = array[cycle]
     
    position = cycle
    for i in range(cycle + 1, len(array)):
      if array[i] < ele:
        position += 1
     
    if position == cycle:
      continue
     
    while ele == array[position]:
      position += 1
    array[position], ele = ele, array[position]
    write += 1
     
    while position != cycle:
       
      position = cycle
      for a in range(cycle + 1, len(array)):
        if array[a] < ele:
          position += 1
       
      while ele == array[position]:
        position += 1
      array[position], ele = ele, array[position]
      write += 1
   
  return write
   
# driver code
array = [2, 4, 5, 1, 3]
print("The original array is:", array)
n = len(array)
cycle_Sort(array)
print("The sorted array is: ",array)


# In[7]:


##Answer2:

def stoogesort(arr, l, h):
    if l >= h:
        return
    if arr[l]>arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t

    if h-l + 1 > 2:
        t = (int)((h-l + 1)/3)

        stoogesort(arr, l, (h-t))

        stoogesort(arr, l + t, (h))

        stoogesort(arr, l, (h-t))

arr = [2, 4, 5, 3, 1]
n = len(arr)
 
stoogesort(arr, 0, n-1)
  
for i in range(0, n):
    print(arr[i], end = ' ')


# In[8]:


##Answer3:

def Pattern(line):
    pat=""
    for i in range(0,line):   
        for j in range(0,line):    
            if ((j == 1 and i != 0 and i != line-1) or ((i == 0 or
                i == line-1) and j > 1 and j < line-2) or (i == ((line-1)/2)
                and j > line-5 and j < line-1) or (j == line-2 and
                i != 0 and i != line-1 and i >=((line-1)/2))): 
                pat=pat+"*"  
            else:     
                pat=pat+" "  
        pat=pat+"\n"  
    return pat

line = 7
print(Pattern(line))


# In[9]:


##Answer4:

n=11

for i in range (n, 0, -1):
    print((n-i) * ' ' + i * '*')


# In[10]:


##Answer5:

def pattern(n):

    for i in range(1,n+1):

        k =i + 1 if(i % 2 != 0) else i

        for g in range(k,n):
            if g>=k:
                print(end="  ")

        for j in range(0,k):
            if j == k - 1:
                print(" * ")
            else:
                print(" * ", end = " ")

n = 10
pattern(n)


# In[11]:


##Answer6:

name = "GIRI"

 
length = len(name)
l = ""
 
for x in range(0, length):
    c = name[x]
    c = c.upper()
     
    if (c == "A"):
        print("..######..\n..#....#..\n..######..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "B"):
        print("..######..\n..#....#..\n..#####...", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "C"):
        print("..######..\n..#.......\n..#.......", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "D"):
        print("..#####...\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..#####...\n\n")
         
    elif (c == "E"):
        print("..######..\n..#.......\n..#####...", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "F"):
        print("..######..\n..#.......\n..#####...", end = " ")
        print("\n..#.......\n..#.......\n\n")
         
    elif (c == "G"):
        print("..######..\n..#.......\n..#.####..", end = " ")
        print("\n..#....#..\n..#####...\n\n")
         
    elif (c == "H"):
        print("..#....#..\n..#....#..\n..######..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "I"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n....##....\n..######..\n\n")
         
    elif (c == "J"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n..#.##....\n..####....\n\n")
         
    elif (c == "K"):
        print("..#...#...\n..#..#....\n..##......", end = " ")
        print("\n..#..#....\n..#...#...\n\n")
         
    elif (c == "L"):
        print("..#.......\n..#.......\n..#.......", end = " ")
        print("\n..#.......\n..######..\n\n")
         
    elif (c == "M"):
        print("..#....#..\n..##..##..\n..#.##.#..", end = " ")
        print("\n..#....#..\n..#....#..\n\n")
         
    elif (c == "N"):
        print("..#....#..\n..##...#..\n..#.#..#..", end = " ")
        print("\n..#..#.#..\n..#...##..\n\n")
         
    elif (c == "O"):
        print("..######..\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "P"):
        print("..######..\n..#....#..\n..######..", end = " ")
        print("\n..#.......\n..#.......\n\n")
         
    elif (c == "Q"):
        print("..######..\n..#....#..\n..#.#..#..", end = " ")
        print("\n..#..#.#..\n..######..\n\n")
         
    elif (c == "R"):
        print("..######..\n..#....#..\n..#.##...", end = " ")
        print("\n..#...#...\n..#....#..\n\n")
         
    elif (c == "S"):
        print("..######..\n..#.......\n..######..", end = " ")
        print("\n.......#..\n..######..\n\n")
         
    elif (c == "T"):
        print("..######..\n....##....\n....##....", end = " ")
        print("\n....##....\n....##....\n\n")
         
    elif (c == "U"):
        print("..#....#..\n..#....#..\n..#....#..", end = " ")
        print("\n..#....#..\n..######..\n\n")
         
    elif (c == "V"):
        print("..#....#..\n..#....#..\n..#....#..", end = " ")
        print("\n...#..#...\n....##....\n\n")
         
    elif (c == "W"):
        print("..#....#..\n..#....#..\n..#.##.#..", end = " ")
        print("\n..##..##..\n..#....#..\n\n")
         
    elif (c == "X"):
        print("..#....#..\n...#..#...\n....##....", end = " ")
        print("\n...#..#...\n..#....#..\n\n")
         
    elif (c == "Y"):
        print("..#....#..\n...#..#...\n....##....", end = " ")
        print("\n....##....\n....##....\n\n")
         
    elif (c == "Z"):
        print("..######..\n......#...\n.....#....", end = " ")
        print("\n....#.....\n..######..\n\n")
         
    elif (c == " "):
        print("..........\n..........\n..........", end = " ")
        print("\n..........\n\n")
         
    elif (c == "."):
        print("----..----\n\n")


# In[12]:


##Answer7:

import datetime 
 
current_time = datetime.datetime.now() 
 
print ("Time now at greenwich meridian is : "
                                    , end = "") 
print (current_time) 


# In[13]:


##Answer8:

import datetime 
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1) 
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)


# In[14]:


##Answer9:

def convert24(str1):

    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
   
    elif str1[-2:] == "AM":
        return str1[:-2]
   
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
          
    else:

        return str(int(str1[:2]) + 12) + str1[2:8]
        
print(convert24("08:05:45 PM"))


# In[ ]:




