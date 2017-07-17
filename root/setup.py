text = ""
with open('main.py') as f:
    text = f.read()
    pass
with open('main') as exe:
    exe.write(compile(text, '', 'exec'))
    pass