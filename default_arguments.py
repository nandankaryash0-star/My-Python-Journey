#def net_price(list_price,discount=0,tax=0.30):
#    return list_price * (1-discount) * (1+tax)

#print(net_price(600,0.45))

import time

def count(start,end):
    for x in range (start,1+end):
        print(x)
        time.sleep(1)
    print("DONE !")

count(1,10 )