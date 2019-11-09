'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name = None, place = None):
    if user_name == None and place == None:
        return "Hello and welcome"
    if place == None:
        return "Hello, " + user_name + ", and welcome"
    if user_name == None: 
        return "Hello and welcome to " + place
    return "Hello, " + user_name + ", and welcome to " + place   


# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list

def list_average(list_number, avg_type = None):
    n = len(list_number)
    if avg_type == "mode":
        for i in list_number:
            list_number.count(i)

    if avg_type == "mean":
        sum(list_number)/len(list_number)
    if avg_type == "median":        
       order = list_number.sort
       return list_number.sort[n/2]
    return sum(list_number)/n
  

