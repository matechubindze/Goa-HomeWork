def delete_elements(main_list, indexes_list):
    indexes_list.sort(reverse=True)
    for i in indexes_list:
        if 0 <= i < len(main_list):
            main_list.pop(i)
    return main_list

main_list = [10, 20, 30, 40, 50]
indexes_list = [1, 3]
result = delete_elements(main_list, indexes_list)
print(result)
