# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 21:23:50 2015
 QuickSort implementation.

Three choices of pivot points are used: (1) The first array element
(2) The last array element
(3) The median between the first, middle, and last array elements
 
@author: LMW
"""

import numpy as np

def ChoosePivot(arr, start_index, end_index, method=1):
    ''' Return array with the selected pivot as the first element in the
    array. Choices:
    1: first element is the pivot
    2: last element is the pivot
    3: median of the first, middle, and last elements is used
    '''
    if method == 1: # pivot is the first element, nothing done
        return
    elif method == 2: # pivot is the last element, swap first and last
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]        
        return       
    else: # pivot is the median of the first, last, and middle elements
        new_arr = arr[start_index:end_index+1]
        if len(new_arr) < 2: # choose first element as pivot point
            return
        else:    
            if len(new_arr)%2 == 0: 
                k = int(len(new_arr)/2) - 1    # if even
            else: k = int(len(new_arr)/2)   # if odd
            
            first = arr[start_index]; last = arr[end_index]; middle = new_arr[k]
            minind = np.argmin([first, last, middle])
            maxind = np.argmax([first, last, middle])
            if minind != 0 and maxind != 0: # choose first as pivot
                return
            elif minind != 1 and maxind != 1: # choose last as pivot
                arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
                return
            else: # choose middle as pivot
                arr[start_index], arr[start_index+k] = arr[start_index+k], arr[start_index]
                return        

def Partition(arr, start_index, end_index, pivotmethod=1):
    ''' Use the partition algorithm, with the pivot set according to
    the choice of pivotmethod (see ChoosePivot for options). 
    Return the index of the pivot point. The input array is updated.
    '''
    ChoosePivot(arr, start_index, end_index-1, pivotmethod)
    p = arr[start_index]  # pivot element
#    print("P = {}".format(p))
    i = start_index+1   # boundary between the <p and >p
    
    for j in range(start_index+1, end_index, 1):
        if arr[j] < p:
#            print(arr[j], arr[i], i, j)
            arr[j], arr[i] = arr[i], arr[j]
#            print(arr[start_index:end_index])            
            i += 1
    arr[start_index], arr[i-1] = arr[i-1], arr[start_index]
#    print(arr[start_index:end_index])
    
    return i
    
def QuickSort_recursive(arr, start_index, end_index, counter, 
                        pivotmethod=1, verbose=False):
    ''' Recursive QuickSort algorithm
    Input: arr = array/list to sort 
        start_index = index of beginning of array elements to be sorted
        end_index = index of end of array elements to be sorted
        counter = array which adds the number of recursive comparisons for
            each call of the Partition function.
        pivotmethod = see ChoosePivot for options, default is the choice of 
            the first element
    '''
    if start_index < end_index:
        
        m_1 = (len(arr[start_index:end_index])-1) # m - 1; number of comparisons
        if m_1 > 0: counter.append(m_1)
        position = Partition(arr, start_index, end_index, pivotmethod)

        if verbose is True:
            print('Number of comparisons in this recursive call: {}'.format(m_1))
            print('Pivot point: {}, Start Index: {}, End Index: {}'.format(\
                arr[position-1], start_index, end_index))
            print('Left array: {}'.format(arr[start_index:position-1]))
            print('Right array: {}'.format(arr[position:end_index]))

        # Left Side of pivot point
        QuickSort_recursive(arr, start_index, position - 1, counter, pivotmethod)
        # Right Side of pivot point
        QuickSort_recursive(arr, position, end_index, counter, pivotmethod)
            
        
def main(fname="QuickSort.txt"):
    ''' Example running the QuickSort_recursive function on the same
    file with different choices of pivot points. The number of recursive
    calls for each choice is printed.
    '''
    print("First Element as Pivot.")
    arr = np.loadtxt(fname)
    counter_firstelement = []
    QuickSort_recursive(arr, 0, len(arr), counter_firstelement, 1)
    print("Recursive Calls = {}".format(sum(counter_firstelement)))
    
    print("Last Element as pivot")
    arr = np.loadtxt(fname)
    counter_lastelement = []
    QuickSort_recursive(arr, 0, len(arr), counter_lastelement, 2)
    print("Recursive Calls = {}".format(sum(counter_lastelement)))
    
    print("Median of First, Middle, and Last as Pivot.")
    arr = np.loadtxt(fname)
    counter_medianelement = []
    QuickSort_recursive(arr, 0, len(arr), counter_medianelement, 3)
    print("Recursive Calls = {}".format(sum(counter_medianelement)))

if __name__ == "__main__":
    main()