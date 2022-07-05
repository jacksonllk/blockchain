
#1) Write a normal function that accepts another function as an argument. 
# Output the result of that other function in your “normal” function.

def division(ela, elb):
    return ela/2, elb/2

def normal_function(division, ela, elb):
    print(division(ela, elb))

normal_function(division, 36, 82)

print(100*'-')


#2) Call your “normal” function by passing a lambda function – 
# which performs any operation of your choice – as an argument.

normal_function(lambda ela, elb: ela + elb, 39, 66)

print(100*'-')

#3) Tweak your normal function by allowing an infinite amount of arguments on which 
# your lambda function will be executed.     

def unlimited_normal_function(division, *arguments):
    for el in arguments:
        print(division(el))
    
unlimited_normal_function(lambda el: el/2, 5,6,7,8,10)

print(100*'-')
 
#4) Format the output of your “normal” function such that numbers look nice and are centered 
# in a 20 character column.

def formatted_unlimited_normal_function(division, *arguments):
    for el in arguments:
        print('Division Result: {:^20}'.format(division(el)))
    
formatted_unlimited_normal_function(lambda el: el/2, 5,6,7,8,10)
