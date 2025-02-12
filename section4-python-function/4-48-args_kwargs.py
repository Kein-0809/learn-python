#! *args: 不特定多数の引数を渡すことが可能. 他のparameterの後に書く
def args_func(*args):
    # argsはtuple型
    print(f"args: {args}")  # -> args: (1, 2, 3, 4, 5)
    
    # unpackして出力
    print("*args:",*args)  # -> *args: 1 2 3 4 5
    
    # 個別の引数を取り出す
    for i, v in enumerate(args):
        print(f"i: {i}, v: {v}")  # -> i: 0, v: 1

args_func(1, 2, 3, 4, 5)
print()

def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args) # listやtupleの合計を求める
    return total / num


average = get_average(1, 2, 3)
print(average)
print()



#! **kwargs: *argsのdictionary版（キーワード付き引数）
def kwargs_func_example(**kwargs):
    print(kwargs)

kwargs_func_example(param1=10, param2=6, param4=4)  # -> {'param1': 10, 'param2': 6, 'param4': 4}
print()


def kwargs_func(**kwargs):
    param1 = kwargs.get('param1', 1)
    param2 = kwargs.get('param2', 2)
    param3 = kwargs.get('param3', 3)

    print({f'param1: {param1}, param1: {param2}, param3: {param3}'})


# 位置引数, キーワード引数, *args, **kwargsの順
def func(positional, keyword='default', *args, **kwargs):
    print(positional, keyword, args, kwargs)


# 引数なしで呼び出すと，keywordはdefault値が入る
kwargs_func()
print()

# param4は関数内で使われていないが，引数として渡すことが可能
kwargs_func(param1=10, param2=6, param3=3, param4=4)
print()

# param4は関数内で使われていないが，引数として渡すことが可能
kwargs_func(param1=10, param2=6, param4=4)
print()


# *と**の正体はunpacking operator
numbers = (1, 2, 3)
print(numbers)  # -> (1, 2, 3) # print((1, 2, 3))と同じ
# "*"をつけると，unpackされて渡される
print(*numbers)  # -> 1 2 3　# print(1, 2, 3)と同じ

print()


a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
# unpackして渡す
c = {**a, **b}  # -> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(c)
