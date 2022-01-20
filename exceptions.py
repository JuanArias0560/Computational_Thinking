
def splits_list_items(list_1,divisor):
    try:
        return [i / divisor for i in list_1]
    except ZeroDivisionError as e:
        print(e)
        return list_1

list_1= list(range(11))
divisor = 0



print(splits_list_items( list_1,divisor))

