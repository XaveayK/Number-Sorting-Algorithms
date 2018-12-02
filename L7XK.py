import ctypes
from time import *
import random


class Sort:
    
    '''
    Constructor
    '''
    def __init__(self, size):
        self._size = int(size) #Establishes the numbers in the array
        self._arr = (size * ctypes.py_object)() #Creates the array
        self._ops = 0 # Extra memory space
        self._Aops = 0 #Array access
        self._Rops = 0 #Recursive calls
        self._elapse = 0 #Elapsed time
    
    '''
    Returns overload
    '''
    def __repr__(self): 
        if self._elapse > 0 or self._ops > 0 or self._Aops > 0 or self._Rops > 0:
            strang = "After sorting:\n" + str(self._arr[:])  
            strang += "\nElapsed time: " + str(self._elapse)
            strang += "\nNumber of Array Acceses: " + str(self._Aops)
            strang += "\nNumber of extra memory Space: " + str(self._ops)
            strang += "\nNumber of recursive function calls: " + str(self._Rops)
        else: strang = "Before sorting:\n" + str(self._arr[:])
        return strang                
    
    '''
    String overload
    '''
    def __str__(self): 
        
        if self._elapse > 0 or self._ops > 0 or self._Aops > 0 or self._Rops > 0:
            strang = str(self._arr[:])  
            strang += "\nElapsed time: " + str(self._elapse)
            strang += "\nNumber of Array Acceses: " + str(self._Aops)
            strang += "\nNumber of extra memory Space: " + str(self._ops)
            strang += "\nNumber of recursive function calls: " + str(self._Rops)
        else: strang = str(self._arr[:])
        return strang        
    
    
    '''
    Purpose: to shuffle the elements of the array to be randomly stored
    '''
    def shuffle(self):
        
        new = (self._size * ctypes.py_object)() #Creates a new array to placehold
        for index in range(self._size): 
            self._arr[index] = index + 1 #Creates items in the array
            new[index] = 0 #Makes each item in the placeholder array zero
        for index in range(self._size):
            ind = random.randint(0, self._size - 1) #Sets an index
            while new[ind] != 0:
                ind = (ind + 1) % self._size #This climbs the ladder of the array
            new[ind] = self._arr[index]
        self._arr = new




class quickSort(Sort):
    
    '''
    Constructor, uses inheritence
    '''
    def __init__(self, size):
        super().__init__(size ) #I learned this for this specific project, an awesome tool
        
    '''
    Purpose: To call recursive quick sort
    '''
    def quickSort(self):
        start = time()
        x = self.recquickSort(self._arr, 0, self._size - 1)
        end = time()
        self._elapse = end - start
        self._arr = x
        
        
    '''
    Purpose: To partition the array
    Paramters: array - the array of items to be organized
               first - the first index in the partition
               last - the last index in the partition
    
    '''
    def partition(self, array, first, last) :
        
        big = first + 1
        small = last
        pivot = array[first]
        self._Aops += 1
        
        
        while (big <= small):
            while (big <= last and array[big] <= pivot): big += 1
            while array[small] > pivot: small -= 1
            if big < small :
                sml = array[big]
                bg = array[small]
                array[big] = bg
                array[small] = sml
                self._Aops += 4
                
        sml = array[first]
        frst = array[small]
        array[first] = frst
        array[small] = sml    
        self._Aops += 4
        
        return small


    '''
    Purpose: To be a recursive call for quick sort
    Paramters: Array - the array of objects to be in place sorted
               first - the first item to be looked at
               last - the last item to be looked at
    Returns: Array - the sorted array
    '''
    def recquickSort(self, array, first, last):
        self._Rops += 1
        if first >= last :
            return
        pivLoc = self.partition(array,first,last)
        
        self.recquickSort(array, first, pivLoc-1)
        self.recquickSort(array, pivLoc+1, last)
        return array    



    
class heapSort(Sort):
    
    '''
    Constructor, uses inheritance
    '''
    def __init__(self, size = 10):
        super().__init__(size)
    
    '''
    Purpose:
    Parameters: myArray - the array being looked at
                last - the 
    '''
    def swapDown(self, myArray, last) :
        insPt = 0
        done = False
        
        while (not done and ((2*insPt+1) <= last)):
            bigChild = 2*insPt + 1
            
            if ((bigChild+1) <= last and
                myArray[bigChild+1] > myArray[bigChild]) :
                self._Aops += 2
                bigChild += 1
                
            if myArray[insPt] < myArray[bigChild] :
                self._Aops += 6
                ins = myArray[insPt]
                bgch = myArray[bigChild]
                myArray[bigChild] = ins
                myArray[insPt] = bgch
                insPt = bigChild           
                
            else:
                done = True
                
    def mergeHeaps(self, myArray, rt) :
        insPt = rt
        done = False
        
        while (not done and ((2*insPt+1) < len(myArray))):
            bigChild = 2*insPt + 1
            
            if ((bigChild+1) < len(myArray) and
                myArray[bigChild+1] > myArray[bigChild]) :
                self._Aops += 2
                bigChild += 1
                
            if myArray[insPt] < myArray[bigChild] :
                self._Aops += 6
                ins = myArray[insPt]
                bgch = myArray[bigChild]
                myArray[bigChild] = ins
                myArray[insPt] = bgch
                insPt = bigChild
                
            else:
                done = True
                
    def buildHeap(self, myArray) :
        lastChild = len(myArray) - 1
        
        for i in range((lastChild-1)//2,-1,-1): #(lastChild-1)//2 parent of lastChild
            self.mergeHeaps(myArray,i)
        
    def heapSort(self):
        start = time()
        self.buildHeap(self._arr)
        for i in range(self._size-1,0,-1):
            self._Aops += 4
            fq = self._arr[0]
            lq = self._arr[i]
            self._arr[0] = lq
            self._arr[i] = fq
            self.swapDown(self._arr,i-1)
            
        end = time()
        self._elapse = end - start



class mergeSort(Sort):
    
    '''
    Constructor, uses inheritance
    '''
    def __init__(self, size):
        super().__init__(size)
    
    
    '''
    Purpose: Calls the recursive mergesort
    '''
    def mergeSort(self):
        start = time()
        self._arr = self.recmergeSort(self._arr)
        end = time()
        self._elapse = end - start
    
    
    '''
    Purpose: To recursively call itself so it can sort into smaller arrays
    Parameters: arr - the array to be sorted
    Returns: arr - the array after it's been sorted
    '''
    def recmergeSort(self, arr):
        
        self._Rops += 1
        
        n = len(arr)
        
        if n <= 1: return arr
        elif n % 2 != 0: arr2 = (((n // 2) + 1) * ctypes.c_int)()
        else: arr2 = ((n // 2) * ctypes.c_int)()
        arr1 = ((n // 2) * ctypes.c_int)()
        self._ops += n
        
        for ind in range(n // 2):
            self._Aops += 4
            arr1[ind] = arr[ind]
            arr2[ind] = arr[ind + (n // 2)]
            
        if n % 2 != 0: arr2[-1] = arr[-1]
        
        arr1 = self.recmergeSort(arr1)
        arr2 = self.recmergeSort(arr2)
        arr = self.merge(arr1, arr2)
        return arr
    
    
    '''
    Purpose: Sorted the array items
    Parameters: l1 - the first array
                      l2 - the second array
    Returns: l - the combined l1 and l2 in correct order
    '''
    def merge(self, l1, l2):#O(n) version
        
        l = ((len(l1) + len(l2)) * ctypes.c_int)()
        ind=0
        i=0
        j=0
        
        while i < len(l1)  and j < len(l2):
            if l1[i] < l2[j]:
                self._Aops += 4
                l[ind]=l1[i] 
                i+=1
                ind+=1
            else: 
                self._Aops += 2
                l[ind]=l2[j]
                j+=1
                ind+=1  
                
        while(i < len(l1)):  
            self._Aops += 2
            l[ind]=l1[i] 
            i+=1
            ind+=1        
            
        while (j < len(l2)): 
            self._Aops += 2
            l[ind]=l2[j] 
            j+=1
            ind+=1	
        return l        

class selectSort(Sort):
    
    '''
    constructor
    '''
    def __init__(self, size):
        super().__init__(size)
    
    '''
    Purpose: To run selection sort algorithm
    '''
    def selectionSort(self):
        start_time = time()
        for ind in range(self._size):
            mini = ind
            
            for index in range(ind + 1, self._size):
                if self._arr[mini] > self._arr[index]:
                    self._Aops += 2
                    mini = index
            
            self._Aops += 4
            frst = self._arr[ind]
            lst = self._arr[mini]
            self._arr[ind] = lst
            self._arr[mini] = frst
            
        end_time = time()
        self._elapse = end_time - start_time
    
    
    
def test(size):
    print("Quick Sort:")
    w = quickSort(size)
    w.shuffle()
    print(w)
    w.quickSort()
    print(w)
    print()
    print()
    print("Heap Sort:")
    x = heapSort(size)
    x.shuffle()
    print(x)
    x.heapSort()
    print(x)
    print()
    print()
    print("Merge Sort:")
    y = mergeSort(size)
    y.shuffle()
    print(y)
    y.mergeSort()
    print(y)
    print()
    print()
    print("Selection Sort:")
    z = selectSort(size)
    z.shuffle()
    print(z)
    z.selectionSort()
    print(z)
    
def main():
    
    while True:
        print("Enter your choice.\n\ta. Merge Sort\n\tb. Quick sort\n\tc. Heap sort\n\td. Selection sort\n\te. Run tests\n\tf. Exit")
        inp = input("Enter your choice: ")
        if inp.lower() == 'a':
            inpu = int(input("Enter the number of elements in the array: "))
            if not isinstance(inpu, int):
                raise TypeError("Number of elements in the array must be integer!")
            sort = mergeSort(inpu)
            sort.shuffle()
            print("Merge Sort")
            print(sort)
            sort.mergeSort()
            print(sort)
            
        elif inp.lower() == 'b':
            inpu = int(input("Enter the number of elements in the array: "))
            if not isinstance(inpu, int):
                raise TypeError("Number of elements in the array must be integer!")
            sort = quickSort(inpu)
            sort.shuffle()
            print("Quick Sort:")
            print(sort)
            sort.quickSort()
            print(sort)
            
        elif inp.lower() == 'c':
            inpu = int(input("Enter the number of elements in the array: "))
            if not isinstance(inpu, int):
                raise TypeError("Number of elements in the array must be integer!")
            sort = heapSort(inpu)
            sort.shuffle()
            print("Heap Sort:")
            print(sort)
            sort.HeapSort()
            print(sort)      
            
        elif inp.lower() == 'd':
            inpu = int(input("Enter the number of elements in the array: "))
            if not isinstance(inpu, int):
                raise TypeError("Number of elements in the array must be integer!")
            sort = selectSort(inpu)
            sort.shuffle()
            print("Selection Sort")
            print(sort)
            sort.selectionSort()
            print(sort)
            
        elif inp.lower() == 'e':
            inpu = int(input("Enter the number of elements in the array: "))
            if not isinstance(inpu, int):
                raise TypeError("Number of elements in the array must be integer!")            
            tests(inpu)
            
        elif inp.lower() == 'f':
            break
        
        else: continue