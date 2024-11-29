fruits = ['apple', 'peach', 'grapes', 'banana']

# enumerateはindexとvalueを同時に取得できる
# デフォルトではindexは0から始まる
for idx, fruit in enumerate(fruits):
    print(f"index: {idx}, fruit: {fruit}")

# enumerateで1つの変数に入れる場合
for x in enumerate(fruits):
    # xはtuple型
    print(x)
