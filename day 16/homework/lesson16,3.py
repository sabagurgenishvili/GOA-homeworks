def even_num(our_list):
    list_even =  ([1,2,3,4,5])
    for i in range(len(our_list)):
        if(our_list[i] % 1) == 0:
            list_even.append(our_list[i])
            return list_even