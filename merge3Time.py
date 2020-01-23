from random import seed
from random import randint
import numpy as np
import time


def main():
    run_time = []
    for i in range(50000,550000,50000):
        array = []
        sum = 0
        temp_runtime =[]
        for j in range(i):
            array.append(randint(0,10000))
        for k in range(3): # run 3 times then average
            temp = array.copy()
            #print(array)
            start_time = time.time()
            mergesort3(temp)
            end_time = time.time() - start_time
            temp_runtime.append(end_time)
            #print(end_time)
            sum += end_time
            #temp.clear()

        temp_runtime.append(sum/3)
        print(temp_runtime)
        string = ""
        for number in temp_runtime:
            string += str(number) + " "
        string += "\n"
        #print(string) 
        run_time.append(string)
        array.clear()
        temp_runtime.clear()
    #print(run_time)
    runtime_file(run_time)

def runtime_file(runtime):
    file = open("merge3time.txt","w")
    file.truncate(0)
    for string in runtime:
        file.write(string)
    file.close()


def mergesort3(array):
    # if the len of the array is less than 2 return
    if len(array) >1:

        mid_lower = len(array) // 3
        mid_upper = 2 * len(array) // 3
        bot = array[0:mid_lower]
        mid = array[mid_lower:mid_upper]
        up = array[mid_upper:len(array)]
        # print (bot)
        # print (mid)
        # print (up)
        # divide, until array size is 1
        mergesort3(bot)
        mergesort3(mid)
        mergesort3(up)
        merge(array,bot,mid,up)


def merge(array,bot,mid,up):
    #conquer
    i = j = k = z = 0 # bot, mid, up, main array
    #comparing all to see what is the smallest between them
    while i < len(bot) and j < len(mid) and k < len(up):
        if bot[i] < mid[j]:
            if bot[i] < up[k]:
                array[z] = bot[i]
                i+=1
            else:
                array[z] = up[k]
                k+=1
            z+=1
        else: # if mid is smaller or up is smaller
            if mid[j] < up[k]:
                array[z] = mid[j]
                j+=1
            else:
                array[z] = up[k]
                k+=1
            z+=1

    # just like mergesort2, merge 1 and 2, 2 and 3, and 1 and 3
    while i < len(bot) and j < len(mid):
        if bot[i] < mid[j]:
            array[z] = bot[i]
            i+=1
        else:
            array[z] = mid[j]
            j+=1
        z+=1
    while j < len(mid) and k < len(up):
        if mid[j] < up[k]:
            array[z] = mid[j]
            j+=1
        else:
            array[z] = up[k]
            k+=1
        z+=1
    while i < len(bot) and k < len(up):
        if bot[i] < up[k]:
            array[z] = bot[i]
            i+=1
        else:
            array[z] = up[k]
            k+=1
        z+=1


    #add the rest of the list back up
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
