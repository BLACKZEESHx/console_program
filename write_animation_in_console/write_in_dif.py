from time import sleep as wt

def write(text,waite=0.1):
    for echar in text:
        print(echar,end="here you can write something to make cool",flush=True)
        wt(waite)

write("""I hope this updated code works for you!""")