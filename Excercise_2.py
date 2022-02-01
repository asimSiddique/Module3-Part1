
def get_combined_dict(dict_1,dict_2):
    my_dict_3 ={}
    for key, value in dict_1.items():
        if key in dict_2:
            sum=dict_1[key]+dict_2[key]
            my_dict_3[key]=sum
    return my_dict_3


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9, 'f':0}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16, 'f':0}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)