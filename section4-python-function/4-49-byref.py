# 参照渡し (byref) <-> 値渡し (byvalue)
# Pythonは参照渡し
def add_nums(a, b):
    print(f"第一引数のID:{id(a)}")
    print(f"第二引数のID:{id(b)}")
    return a + b


one = 1
two = 2
# oneは1, twoは2というオブジェクトを参照している
print(id(one))
print(id(two))
# add_nums内でも1, 2というオブジェクトを参照しているのでidは同じ
add_nums(one, two)
print()

# immutableでは変数を更新できないので値渡しのような挙動をする (実際は参照渡し)
def add_one(num):
    # 引数で受け取った変数のアドレスを参照 (値を参照しているわけではない
    print(f"変更前のID:{id(num)}")
     # 値を更新する (メモリ内にある新しいアドレスに新しいオブジェクトを作成する)
    num += 1
    # 先程作った新しいアドレスを参照する
    print(f"変更後のID:{id(num)}")
    return num


one = 1
print(f'関数呼び出し前のone:{one}')
print(f"関数呼び出し前のID:{id(one)}")
add_one(one)
print(f'関数呼び出し後のone:{one}')
print(f"関数呼び出し後のID:{id(one)}")
print()

# mutableでは変数を更新できるので(そのまま)参照渡しの挙動となる
def add_fruit(fruits, fruit):
    # 引数で受け取った変数のアドレスを参照 (値を参照しているわけではない)
    print(f"変更前のID:{id(fruits)}")
    # そのまま現状のアドレスを使用したまま値を更新する (新しいアドレスで新しいオブジェクトを作成しない)
    fruits.append(fruit)
    # 先程更新したアドレスの状態を参照する
    print(f"変更後のID:{id(fruits)}")
    return fruits


myfruits = ['apple', 'banana', 'peach']
myfruit = 'lemon'
print(f'関数呼び出し前のmyfruits{myfruits}')
add_fruit(myfruits, myfruit)
# "add_fruit"関数によって参照先のアドレスにある値が更新されたため、
# 関数呼び出し後のmyfruitsも更新されている
print(f'関数呼び出し後のmyfruits{myfruits}')

# immutableは値渡しのような挙動をする (実際は参照渡し)
# mutableは参照渡しの挙動をする
