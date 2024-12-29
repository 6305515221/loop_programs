#replace vowels with *
'''
a='python selenium'
i=0
s=''
while i<len(a):
    if(a[i] in 'AEIOUaeiou'):
        s=s+"*"
    else:
        s=s+a[i]
    i+=1
print(s)

a='python selenium'
i=0
while i<len(a):
    if(a[i] in 'AEIOUaeiou'):
        print("*",end="")
    else:
        print(a[i],end="")
    i+=1
output:pyth*n
'''

#using replace method
'''
a='python'
i=0
while i<len(a):
    if(a[i] in 'AEIOUaeiou'):
        s=a[i].replace(a[i],"*")
        print(s,end='')
    else:
        print(a[i],end='')
    i+=1
'''

#given string having palindrom
'''
a=input().split()
i=0
l=[]
while i<len(a):
    if(a[i]==a[i][::-1]):
        l+=[a[i]]
    i+=1
print(l)
 output:
pavan mom dad
['mom', 'dad']
'''

#a=['hai',3,'2..4']
'''
a=input().split()
i=0
while i<len(a):
    if isinstance(a[i],int):
        print(a[i])
    i+=1
'''
a='this is pavan'.split()
print(a)
i=0
while i<len(a):
    print(zip(a[i],len(a[i])))
