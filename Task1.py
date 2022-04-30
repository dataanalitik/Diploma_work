def filter_list(lst):
    new_list = []
    for x in lst:
        if type(x) == int:
            new_list.append(x)
    return new_list


print(filter_list([1, 'ryht', 'ervge', 'rewfe', 6]))
print(filter_list([1, 5, 52, 'bsfb']))
