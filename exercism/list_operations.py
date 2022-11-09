def append(list1, list2):
    return list1 + list2


def concat(lists):
    concat_list = []
    for x in lists:
        for y in x:
            concat_list.append(y)
    return concat_list


def filter(function, list):
    filter_list = []
    for x in list:
        if function(x):
            filter_list.append(x)
    return filter_list


def length(list):
    len = 0
    for x in list:
        len += 1
    return len


def map(function, list):
    result = []
    for x in list:
        result.append(function(x))
    return result


def foldl(function, list, initial):
    result = initial
    for x in reverse(list):
        result = function(result, x)
    return result


def foldr(function, list, initial):
    result = initial
    for x in reverse(list):
        result = function(x, result)
    return result


def reverse(list):
    return list[::-1]
