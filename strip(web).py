import re

def strip(text,chars=None):
    """去除首尾的字符
:type text:string
:type chars:string
:rtypr:string
"""
    if chars is None:
        reg = re.compile('^*|*$')
    else:
        reg = re.compile('^['+chars+']*|['+chars+']*$')
    return reg.sub(' ',text)


print(strip('     123456      '))
print(strip('      123456'))
print(strip('123456    654321','1'))

