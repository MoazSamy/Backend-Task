def fill_array():
    # Requesting the size of the array
    n = int(input("Please enter the size of the array:"))
    
    #Checking for valid n size
    if n < 2:
        print("Invalid input , required input >= 2")
        
        # Rerunning the function because of invalid input
        fill_array()
        
    else:
        # Defining the list and filling it
        array = [int(i) for i in input("Please enter your desired numbers:").split()][:n]
        
        # Rerunning input in case of invalid input
        while(len(array) != n):
            print("invalid input , required input = desired size")
            array = [int(i) for i in input("Please enter your desired numbers:").split()][:n]
        return array

# Assigning values
array = fill_array()
n = len(array)
 
# Using Python's timsort , since it's a better version of mergesort
array.sort()
 
# Finding absolute minimum value
min_value = abs(array[0]-array[1])
for i in range(1,n-1) :
     curr_value = abs(array[i] - array[i+1])
     if curr_value < min_value:
         min_value = curr_value

#Printing
print(f"\nThe absoulte minimum difference found : {min_value}")

