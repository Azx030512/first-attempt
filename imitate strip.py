#!python3
#imitate strip()
def fakestrip(text,mark=None):
    import re
    exam1=re.compile(r'(\s*)(.*)(\s*)')
    if mark==None:
        mo=exam1.search(text)
        text=mo.group(2)
        return text
    if mark!=None:
        exam2=re.compile(mark)
        return exam2.sub('',text)
print(fakestrip('     123456     '))
print(fakestrip('123456    123654321','123'))
print(fakestrip('The cat sat on the mat.','a'))
