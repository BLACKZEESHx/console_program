from time import sleep as wt

def write(text,waite=0.1):
    for echar in text:
        print(echar,end="__",flush=True)
        wt(waite)

write("""\tI hope this updated code works for you!\t""")