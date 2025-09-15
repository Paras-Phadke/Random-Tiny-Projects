import time
import sys

def printwipe(text,delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

tex1t = "Hello world"
printwipe(tex1t)
