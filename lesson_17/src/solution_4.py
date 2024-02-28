from typing import List, Dict

def sort_objects(data: List[Dict[str, int]], key_1: str):
    print(sorted(data, key = lambda item: item[key_1]))
    

sort_objects([{'a':3, 'b':7, 'c':8}, {'a':20, 'b':2, 'c':5}, {'a':9, 'b':1, 'c':2}], 'a')
sort_objects([{'a':3, 'b':7, 'c':8}, {'a':20, 'b':2, 'c':5}, {'a':9, 'b':1, 'c':2}], 'b')
sort_objects([{'a':3, 'b':7, 'c':8}, {'a':20, 'b':2, 'c':5}, {'a':9, 'b':1, 'c':2}], 'c')



#def sort_objects(data: List[Dict[str, int]], key_1: str):
#    result_dict = {}
#    result_list = []
#    key_index = 0
#    for dict_i in data:
#        if key_1 not in dict_i:
#            message = 'Нет такого ключа в словарях'
#            return message
#        for key, value in dict_i.items():
#            if key == key_1:
#                result_dict[value] = key_index
#                key_index += 1
#    sorted_dict = dict(sorted(result_dict.items()))
#    for value_i in sorted_dict.values():
#        result_list.append(data[value_i])
#    return result_list