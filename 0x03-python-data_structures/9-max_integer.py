#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == " ":
        return None
        
    else:
        maxi = my_list[0] 
        for i in my_list:
          if my_list[i] > my_list[i+1]:
                return my_list[i]
