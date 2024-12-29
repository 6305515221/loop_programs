#program to iterate any iterable
'''
s= 'python'
#print(' '.join(s))
for i in s:
    print(i,end='')
'''
#to get keys values items from dictionary
'''
d={'python':10,
   'java':20,
   'c':30,
   'css':40}
for i in d.keys(): 
    print(i)
#output:python java c css
    
for i in d.values():
    print(i)
#output:10 20 30 40
    
for i in d.items():
    print(i)
#output:('python', 10) ('java', 20)('c', 30) ('css', 40)
for i,j in d.items():
    print(i,j)

    #or using index
for i in d.items():
    print(i[0],i[1])
'''

#break
'''
i=0
while i<10:
    if i==5 :
        break
    else:
        print(i)
    i+=1
output:01234
'''
#continue
'''
t=(1,2,3,4)
for i in t:
    if(i%2==0):
        continue
    else:
        print(i)
output:13
'''
#pass
'''
for i in [4,5,6]:
    pass
for i in "hai":
    print(i)
output:h a i
'''


#range
'''
r1=range(1,11)
print(list(r1))
'''

#left to right positive
#right to left negative
#program to print 10 to 1
'''
for i in range(10,0,-1):
    print(i,end=' ')
print() #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
#program to print -10 to -1
'''
for i in range(-10,0):
    print(i,end=" ")
print() #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
'''
#program to print -10 to 5
'''
for i in range(-10,6):
    print(i,end=" ")
print() #-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0 1 2 3 4 5
'''
#program to print -10 to -20
'''
for i in range(-10,-21,-1):
    print(i,end=" ")
print() #-10 -11 -12 -13 -14 -15 -16 -17 -18 -19 -20 
'''

#program to print 20 to -15
'''
for i in range(20,-16,-1):
    print(i,end=" ")
print() #20 to -15
'''
#program to print -20 to -15
'''
for i in range(-20,-14):
    print(i,end=" ")
print() #-20 -19 -18 -17 -16 -15
'''
#program to get only even numbers from user input
'''
n=int(input("enter the start number"))
m=int(input("enter the end number"))
for i in range(n,m+1):
    if(i%2==0):
        print(i,end=" ")
print()
output:
enter the start number10
enter the end number20
10 12 14 16 18 20
'''
#program to get the word and index using for loop
'''
n=input().split()
for i in n:
    print(i,n.index(i))


output:

pavan kumar dd
pavan 0
kumar 1
dd 2

#or

n=input().split()
t=()
for i in range(len(n)):
    t=t+((i,n[i]),)
print(t)

output:((0, 'pavan'), (1, 'kumar'))
'''

#enumerate
'''
s=input().split()
#print(tuple(enumerate(s)))#((0, 'pavan'), (1, 'kumar'))
#print(enumerate(s)) # if you use this its shows output and adrres
#print(list(enumerate(s))) #[(0, 'pavan'), (1, 'junb')]



for i in enumerate(s):
    print(i)

#if you want start with 1 you give s,1 in range
'''
#create a tuple with index and length of each words
'''
s=input().split()
for i,word in enumerate(s):
    print((i,len(word)))

s=input().split()
for i in s:
    print((s.index(i),len(i)))
'''
#or
'''
s="hello guys good morning".split()
a=tuple(s)
t=()
for i in range(len(a)):
    t=t+(i,a[i],len(a[i]))
print(t)

#or
s="hello guys good morning"
t=()
for i,word in enumerate(s.split()):
    t=t+((i,len(word)),)
print(t)#((0, 5), (1, 4), (2, 4), (3, 7))
'''
#create a set with index and word only with even length
'''
s=input().split()
for i,word in enumerate(s):
    if(len(word)%2==0):
        print({i,word,len(word)})
#or
s=input().split()
for i in s:
    if(len(i)%2==0):
        print({s.index(i),i})
'''
'''
s="hello guys good morning"
t=()
for i,word in enumerate(s.split()):
    if(len(word)%2==0):
        t=t+((i,len(word)),)
print(set(t)) #{(2, 4), (1, 4)}


a="hello guys good morning"
s=set()
for i,word in enumerate(a.split()):
    if(len(word)%2==0):
        s.add(word)
print(s) #{'guys', 'good'}
'''
#create a dictionary with square of index and first char of words
'''
s={"pavan":3,"kumar":2,"cat":4}
l=list(s)
for i in l:
    print((l.index(i)**2,i[0]))

output:
(0, 'p')
(1, 'k')
(4, 'c')
#or user input
a=int(input("enter the no.of items"))
d={}
for i in range(a):
    keys=input("enter the keys")
    values=int(input("enter the values"))
    d[keys]=values
    s=list(d)
for j in s:
    print((((s.index(j)**2),j[0])))

output:
enter the no.of items3
enter the keyspavan
enter the values1
enter the keyskumar
enter the values2
enter the keystiger
enter the values3
(0, 'p')
(1, 'k')
(4, 't')

'''
#create a dict with charater and index
'''
a='pavan is a good boy'.split()
d={}
for i in a:
    d[i]=a.index(i)
print(d)
 output:
{'pavan': 0, 'is': 1, 'a': 2, 'good': 3, 'boy': 4}

'''


#create a dict with last char of word and index which is its cube
'''
a=input().split()
d={}
for i in a:
    d[i[len(i)-1]]=a.index(i)**3
print(d)

output:
pavan is a good boy
{'n': 0, 's': 1, 'a': 8, 'd': 27, 'y': 64}

a=int(input("enter the no.of items"))
d={}
for i in range(a):
    keys=input("enter the keys")
    values=int(input("enter the values"))
    d[keys]=values
    l=list(d)
    s={}
    for i in l:
        s[i[len(i)-1]]=(l.index(i)**3)
print(s)
'''  
# create a list with elements and it's index and datatype in tuple (index, datatype
'''
s=[1,"pavan",[10,20],(1,2)]
#s=input("enter the string").split()
for i in s:
    print(((type(i),s.index(i))))

'''
# create a tuple with even index and elements
'''
a=input().split()
print((a[::2]))
'''
        
# create a list with index and last char elements
'''
a=input().split()
for i in a:
    print(a.index(i),i[len(i)-1])
output:pavan kumar
0 n
1 r
'''
# create a set with squared index and elements length
'''
a=input().split()
for i in a:
    print({a.index(i)**2,len(i)})

output:
pavan 10 roo
{0, 5}
{1, 2}
{3, 4}
'''
# create a dictionary with character and index if the index is odd
'''
a={'a':1,'b':2,'c':3,'d':4,'e':5}
l=list(a)
for i in l:
    if(l.index(i)%2!=0):
        print((i,l.index(i)))
output:
('b', 1)
('d', 3)

#output should br in dict
a={'a':1,'b':2,'c':3,'d':4,'e':5}
l=list(a)
d={}
for i in l:
    if(l.index(i)%2!=0):
        d[i]=l.index(i)
print(d)

output:
{'b': 1, 'd': 3}

'''

#zip and zip_longest
'''
s="exam's"
l=[True,4,5.6,]
from itertools import zip_longest
for n in zip_longest(s,l):
    print(n,end="")  #('e', True)('x', 4)('a', 5.6)('m', None)("'", None)('s', None)
for n in zip_longest(s,l,fillvalue='a'):
    print(n,end="")  #('e', True)('x', 4)('a', 5.6)('m', 'a')("'", 'a')('s', 'a')
'''
'''
#l=[1,2,3,4]
#s=[1,2,3,4]
l=list(input())
s=list(input())
from itertools import zip_longest
for i,j in zip_longest(l,s):
    print(f'{int(i)}+{int(j)}={int(i)+int(j)}')
'''
#program to square the number in t

'''
s=input().split()
l=input().split()
from itertools import zip_longest
for i,j in zip_longest(l,s):
    #print(((int(i)**2),(int(j)**3)))
     print((f'({int(i)**2},{int(j)**3})'))
'''
