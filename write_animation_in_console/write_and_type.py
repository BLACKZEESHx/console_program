import time

def write_animation(text):
    for i in range(len(text)):
        print(text[:i+1], end='\r', flush=True)
        time.sleep(0.1) # adjust the delay as needed
    # print()

# example usage
write_animation("Hello, world!")
time.sleep(1) # add a pause before modifying the text
write_animation("My Name is Abdullah")
time.sleep(5) # add a pause before modifying the text