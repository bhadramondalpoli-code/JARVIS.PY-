from random import randint as h
l=[]
n=input('Enter the word: ')
while True:
            s=''
            for j in range(len(n)):
                f=h(0,len(n)-1)
                if n.count(n[f])>s.count(n[f]):
                    s+=n[f]
                else:
                    break
            if s not in l and len(s)==len(n):
                l.append(s)
                print(s)
