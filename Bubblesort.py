
#Bubble sort is all about sorting the array in ascending order

def sort(list):

    for i in range(0,len(list)):
        for j in range(i+1,len(list)):

            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp



list= [1,5,8,9,2,4]

print(list)                        #Printing the list before sorting

#print(sorted(list))                # Inbuilt function to sort the list/array

sort(list)

print(list)                        #Printing the list after sorting
