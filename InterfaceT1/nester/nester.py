"""
判断列表是否包含列表
通过循环使所有的列表数据迭代出来
"""
def print_lol(lists):
    """传一个列表参数，"""
    for each_list in lists:
        if isinstance(each_list, list):
            print_lol(each_list)
        else:
            print(each_list)
