#Input a list of numbers and swap elements at the even location with the
#elements at the odd location.


#creating the list
n=int(input("How many numbers due you want to print? "))
list1=[]
for i in range(0, n): 
    a = int(input("Enter the number here:")) 
    list1.append(a)
print("The original list is: ",list1)

#swapping
for i in range(0,len(list1)-1,2):
    list1[i],list1[i+1]=list1[i+1],list1[i]
print("The updated list is: ", list1)
