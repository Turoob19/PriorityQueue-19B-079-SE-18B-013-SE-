#IMPLEMENTING MAX PRIORITY QUEUE


#GITHUB LINK
#https://github.com/Turoob19/PriorityQueue-19B-079-SE-18B-013-SE-/blob/main/README.md


class HeapPQ:
    def __init__(self,inf):
        self.tree_array= 20
        self.heap_size= 0
        self.heap_array= [None] * self.tree_array
        self.inf= inf


    def Root(self):
        # checking if there is any element in the queue
        if len(self.heap_array)==0:
            return "Heap is Empty"
        #return the root or 1st element of the queue
        return self.heap_array[1]

    def Parent(self,ind):
         # checking if there is any element in the queue
        if len(self.heap_array)==0:
            return "Heap is Empty"
        #return the parent index of any node
        return ind//2

    def GetLeftChild(self,ind):
        #check if the length of the array is greater than the index we provided
        if ind >= 1 and len(self.heap_array) > (2*ind):
            #return the left child
            return 2*ind
        return -1

    def GetRightChild(self,ind):
         #check if the length of the array is greater than the index we provided
        if ind >= 1 and len(self.heap_array) > (2*ind +1):
            #return the right child
            return 2*ind +1
        return -1


    def Increase_Key(self,ind,k):
        #checking if the input key is less than undex value in the priority queue
        if k < self.heap_array[ind]:
            return "Error"
        
        self.heap_array[ind]= k
        #comparing the values of the index and swaping if the condition is true
        while ind > 1 and self.heap_array[self.Parent(ind)] < self.heap_array[ind]:
            self.heap_array[ind],self.heap_array[self.Parent(ind)]= self.heap_array[self.Parent(ind)],self.heap_array[ind]
            ind= self.Parent(ind)

    def Decrease_Key(self,ind,k):
        #checking if the input key is greater than undex value in the priority queue 
        if k > self.heap_array[ind]:
            return "Error"
        #setting the input k in the array and
        #using max heapify to maintain the max heap property
        self.heap_array[ind]=k
        self.Max_Heapify(ind)


    def Max_Heapify(self,ind):
        L= self.GetLeftChild(ind)
        R= self.GetRightChild(ind)
        #providing the variable to the input index
        large= ind
        #comparing the left node index with heap size and heap index 
        if ((L <= self.heap_size) and (self.heap_array[L] >self.heap_array[ind])):
            if L>0:
                large= L
        #comparing the right node index with heap size and heap index 
        if ((R <= self.heap_size) and (self.heap_array[R] > self.heap_array[large])):
            if R>0:
                large= R
       #swaping if the given condition satisfy
        if large != ind:
            self.heap_array[ind],self.heap_array[large]=self.heap_array[large],self.heap_array[ind]
            self.Max_Heapify(large)

            
   # finds the highest value from the heap and
   #pop out that value
    def Extract_Max(self): # Dequeue
        if self.heap_size < 1:
            return "Heap underflow"
        
        max_value=self.heap_array[1]
        self.heap_array[1]= self.heap_array[self.heap_size]
        self.heap_size= self.heap_size - 1
        self.Max_Heapify(1)
        print (max_value,"has been deleted")

   #insert the key value in o(1)
    def Enqueue(self,k):
        self.heap_size= self.heap_size +1
        self.heap_array[self.heap_size]= -1*(self.inf)
        self.Increase_Key(self.heap_size,k)
        
    #print the  max value of the heap array or priority queue
    def Get_Maximum(self):
        print ("Maximum value of the Priority Queue: ",self.heap_array[1])

     # build a heap with an unordered array
    def Built_Max_Heap(self):
        for i in range(self.heap_size//2, 0 ,-1):
            self.Max_Heapify(i)
            
    #Get the minimum value of the priority queueu        
    def Get_Minimum(self):
        n= self.heap_size
        minimum_value= self.heap_array[n//2]
        for i in range((1+n)//2,n):
            minimum_value= min(minimum_value, self.heap_array[i])
        print("Minnimum Element of the Priority Queue: ",minimum_value)
        
        
    #print all the inserted values
    def Print(self):
        print (list(self.heap_array[1:self.heap_size +1]))
        

    

obj= HeapPQ(10000)
obj.Enqueue(1)
obj.Enqueue(2)
obj.Enqueue(3)
obj.Enqueue(4)
obj.Enqueue(5)
obj.Enqueue(6)
obj.Enqueue(7)
obj.Enqueue(8)
obj.Enqueue(9)
obj.Enqueue(10)
obj.Extract_Max()
obj.Print()
obj.Get_Maximum()
obj.Get_Minimum()
print("The Root node of this heap is: ", obj.Root())
print("The Parent index is: ",obj.Parent(4))
print("The Left child index is: ",obj.GetRightChild(4))
print("The Right child index is: ",obj.GetLeftChild(4))





