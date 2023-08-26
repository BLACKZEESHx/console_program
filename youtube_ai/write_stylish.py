from time import sleep as wt
import pyfiglet


def write_like_gpt(text,waite=0.1):
    for echar in text:
        print(echar,end="",flush=True)
        wt(waite)
    print()

def write_in_underline(text,waite=0.1):
    for echar in text:
        print(echar,end="_",flush=True)
        wt(waite)
    print()

def write_in_mono(text,waite=0.1):
    for echar in text:
        print(echar,end=" ",flush=True)
        wt(waite)
    print()

def write_in_ascii(text:str)->str:
    # Use pyfiglet to convert the text to ASCII art
    ascii_art = pyfiglet.figlet_format(text)
    # typing the ASCII art to the console
    write_like_gpt(ascii_art)


def write_in_3d_underline(text,waite=0.1):
    for echar in text:
        print(echar,end="__",flush=True)
        wt(waite)
    print()


def overwrite_typing(text):
    for i in range(len(text)):
        print(text[:i+1], end='\r', flush=True)
        wt(0.1) # adjust the delay as needed
    print()

