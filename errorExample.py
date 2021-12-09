def spam():
    bacon()
def bacon():
    raise Exception('This is the wrong message !')
spam()
