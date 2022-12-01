def sequential_map(*args):
    *functions_list, container = args
    for function in functions_list:
        result_list = list(map(function, container))
    return result_list


def consensus_filter(*args):
    *functions_list, container = args
    for func in functions_list:
        container = list(filter(func, container))
    return container


def conditional_reduce(*args):
    *functions, container = args
    first, *remain_list = list(filter(functions[0], container))
    for remain in remain_list:
        first = functions[1](first, remain)
    return first


def func_chain(*args):
    def chain_in_chain(x):
        for function in args:
            res = function(x)
        return res
    return chain_in_chain
