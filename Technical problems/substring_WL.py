def is_substring(s1 ,s2):
    # Converting the strings to lists.
    l1= list(s1)
    l2= list(s2)
    
    # Initializing values.
    cond = True
    i=0
    
    # While looping one char from s1 over the chars from s2 then poping it
    # if it doesn't match.
    while(cond):
        if len(l1) == 0:
            cond=False
        else:
            if l1[0]==l2[i]:
                return True
            else:
                i+=1
                if i == len(l2):
                    l1.pop(0)
                    i=0
    return False



s1 = input("Enter your first string:")
s2 = input("Enter your second string:")
state = is_substring(s1,s2)
if (state == True):
    print("\nYES")
else:
    print("\nNO")