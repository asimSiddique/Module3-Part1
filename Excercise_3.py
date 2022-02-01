#https://stackoverflow.com/questions/40985203/counting-letter-frequency-in-a-string-python
# I saw the counter method on this post on stack overflow. Counter is dict subclass that allow us to count hashable objects. 
# however it did not give me lower case letters or removed spaces. So I manually manipulated the string so all letters are lowercase and all the spaces are removed. Then I had figure out how to turn a counter 
# into dict because it kept giving me counter({}) as output. So I iterated over that counter dict, put it into another dict and returned that. 


import collections

def string_counter(my_string):
    dict={}
    my_string = my_string.lower()
    my_string =my_string.replace(" ","")
    print(my_string)
    count= collections.Counter(my_string)
    for key, value in count.items():
        dict[key] = value
    return dict
    

user_input = input("Enter a String: ")
print(string_counter(user_input))
