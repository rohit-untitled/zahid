def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array) - i - 1):
            if array[j]>array[j+1]:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
data=[5,1,4,2,8]
bubbleSort(data)
print('Sorted array in Ascending Order:')
print(data)