#!python3
#P146.7.18.2

def mightyDirection(text):
    import  re
    exam1=re.compile(r'.{8,}')
    exam2=re.compile(r'[A-Z]')
    exam3=re.compile(r'[a-z]')
    exam4=re.compile(r'\d')
    container1=[]
    for i in text:
        container1.append(i)
    container2=' '.join(container1)
    print(container1)
    print(container2)
    A=exam1.search(text)
    print(A)
    B=exam2.search(container2)
    print(B)
    C=exam3.search(container2)
    print(C)
    D=exam4.search(container2)
    print(D)
    if A and B and C and D :
        print('This is mighty direction !')
        return True
    else:
        print('This  is not mighty direction !')
        return False
print('Please type mighty direction which contains capital word,little word,digits and the length is more than 7')
mightyDirection(input())
        
