import os

def start(file, source):
    data = ""
    with open(file) as f:
        data = f.read()
    lines = data.split('\n')
    ext = []
    arg = []
    for line in lines:
        if line.startswith('form'):
            c = (line.split()[1], line.split()[2])
            ext.append(c)
            pass
        elif line.startswith('arg'):
            c = (line.split()[1], line.split()[2])
            arg.append(c)
            pass
    for s in ext:
        ex = s[0]
        cm = s[1]
        a = ''
        for ar in arg:
            if ar[0] == cm:
                a = ar[1]
        print('Running ' + cm)
        os.system(cm + ' '+source+'/*.' + ex + ' ' + a.replace('~', ' '))
        pass
    pass

#Starting application
x = input('Enter file name: ')
src = input('Enter sources directory: ')
start(x, src)