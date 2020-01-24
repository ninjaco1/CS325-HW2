import random
import numpy as np
import time
import os

#where all the functions are called
def main():
    data = open("data.txt", "r")
    line = data.readlines()
    data.close()
    #print(line)
    array = []
    # loop through each line and sort and append each line into array
    for j in range(len(line)):
        temp = [int(i) for i in line[j].split() if i.isdigit()]
        temp.pop(0)
        mergesort3(temp)
        array.append(temp)

    #print(array)

    #insert sorted data value in a different file
    out_file(array)

    # array = [1,5,2,6,9,0,8,3,7]
    # print (array)
    # # mergesort(array, 0, len(array)-1)
    # mergesort(array)
    # print (array)

# where the sorted array gets outputted to a file
def out_file(array):
    out = open("merge3.txt", "w")
    out.truncate(0)
    for i in range(len(array)):
        write = ""
        for number in array[i]:
            write += str(number) + " "
        write += "\n"
        out.write(write)
    #print(write)
    out.close()

#mergesort 3
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

#merges 3 arrays together into one
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
