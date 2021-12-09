def swap(number):
    import re
    Regex=re.compile(r'(\d)(\d)(\d)')
    mo=Regex.search(number)
    result=''
    for i in range(1,4):
        result+=mo.group(4-i)
    print(result)
    return None
number=input()
swap(number)

        
