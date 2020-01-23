from random import seed
from random import randint
import numpy as np
import time


def main():
    array = []
    for i in range(10):
        array.append(randint(0,100))
    print (array)
    mergesort3(array)
    print(array)



def mergesort3(array):
    # if the len of the array is less than 2 return
    if len(array) >1:

        mid_lower = len(array) // 3
        mid_upper = 2 * len(array) // 3
        bot = array[0:mid_lower]
        mid = array[mid_lower:mid_upper]
        up = array[mid_upper:len(array)+1]
        print (bot)
        print (mid)
        print (up)
        # divide, until array size is 1
        mergesort3(bot)
        mergesort3(mid)
        mergesort3(up)

        #conquer
        i = j = k = z = 0 # bot, mid, up, main array

        




        while i < len(bot):
            array[z] = bot[i]
            i += 1
            z += 1
        while j < len(mid):
            array[z] = mid[j]
            j += 1
            z += 1
        while k < len(up):
            array[z] = up[k]
            k += 1
            z += 1







main()
