"""
Write a function, dictdiff, that takes two dicts as arguments. The function returns  a new dict that expresses the difference between the two dicts.  If there are no differences between the dicts, dictdiff returns an empty dict. For  each key-value pair that differs, the return value of dictdiff will have a key-value pair  in which the value is a list containing the values from the two different dicts. If one of  the dicts doesn’t contain that key, it should contain None. The following provides some  examples:
"""


def dict_diff(dic1, dic2):
    # output = {}

    # all_keys = dic1.keys() | dic2.keys()

    # for key in all_keys:
    #     if dic1.get(key) != dic2.get(key):
    #         output[key] = [dic1.get(key), dic2.get(key)]

    # return output

    # or

    # return {
    #     key: [dic1.get(key), dic2.get(key)]
    #     for key in [i for i in dic1.keys()] + [i for i in dic2.keys()]
    #     if dic1.get(key) != dic2.get(key)
    # }

    # or

    # return {
    #     key: [dic1.get(key), dic2.get(key)]
    #     for key in dic1.keys() | dic2.keys()
    #     if dic1.get(key) != dic2.get(key)
    # }

    # or

    return {
        key: [dic1.get(key), dic2.get(key)]
        for key in {**dic1, **dic2}
        if dic1.get(key) != dic2.get(key)
    }


d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 2, "c": 4}
print(dict_diff(d1, d1), {})
print(dict_diff(d1, d2), {"c": [3, 4]})

d3 = {"a": 1, "b": 2, "d": 3}
d4 = {"a": 1, "b": 2, "c": 4}
print(dict_diff(d3, d4), {"c": [None, 4], "d": [3, None]})

d1 = {"a": 1, "b": 2, "c": 3}
d5 = {"a": 1, "b": 2, "d": 4}
print(dict_diff(d1, d5), {"c": [3, None], "d": [None, 4]})
