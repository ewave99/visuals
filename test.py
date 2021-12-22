import time
import os
import math 
t = lambda: time.clock_gettime(time.CLOCK_REALTIME)

def rp(f=lambda x: x, thickness=1):
    size = os.get_terminal_size()
    x = int(f(t())*size.columns)
    print ( ' '*(x-thickness)+'x'*thickness+' '*(size.columns-x-thickness))

def sinrp(stretch):
    rp(lambda x: math.sin(stretch*x)/2+1/2, stretch*3)

while True:
    stretch=2
    rp(lambda x: math.sin(stretch*x)/4 + math.sin(2 * stretch * x )/4+1/2, stretch*3)
    time.sleep(0.05)
