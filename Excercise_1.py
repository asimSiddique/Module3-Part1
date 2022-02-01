def get_unique_list(integer):
    second_list=[]
    for i in integer:
        if i  not in second_list:
            second_list.append(i)
    return second_list


my_list = [1, 2, 3, 2, 1, 4,5,409,5,3,7,4,3,4,4,5,8,9,3,2,6,8,9,5,5,8,3,7,8,45,55,3,-1,-1,-2,0.6,0.6,0.7]
unique_list = get_unique_list(my_list)
print(unique_list)