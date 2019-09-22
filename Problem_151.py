import random
import numpy as np

result = []

def job():

    envelope = [16]
    counter = 0

    while envelope:
        table = []
    
        if len(envelope) == 1 and envelope[0] != 16:
            counter += 1
        if envelope[0] == 1 and len(envelope) == 1:
            break
            
        table.append(envelope.pop(random.randint(0,len(envelope)-1)))

        while True:
            if 1 in table:
                table.remove(1)
                envelope += table
                break
            else:
                table += [int(table.pop()/2)]*2

    return counter - 1
