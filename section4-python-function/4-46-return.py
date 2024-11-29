# returnしない関数を作ることもできる
def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f"key: {k}, value: {v}")

a = {"one": 1, "two": 2}
print(a)
print_dict(a)

print()

# returnしない関数は，Noneをreturnしている．
return_value = print_dict(a)
print(return_value)  # None ("print_dict"関数内でprintしているので，返り値が無いためNoneになる)

print()


# 複数returnする場合は,(カンマ)で区切って渡す
def get_first_last_word(text):
    text = text.replace(",", "")
    words = text.split()
    return words[0], words[-1]  # "words[0]"と"words[-1]"を返す


text = "Hello, My name is Mike"
# 複数戻り値があると，tuppleで渡される
print(get_first_last_word(text))  # ('Hello', 'Mike')

print()

# 複数戻り値があると，tuppleで渡されるので，unpackで受け取る
first, last = get_first_last_word(text)  # "words[0]"と"words[-1]"をunpackして受け取る
print(f'first word is {first}, last word is {last}')

print()

# Turpleの復習
a, b, c = (1, 2, 3)
print(f"Turpleの復習\na: {a}, b: {b}, c: {c}")  # a: 1, b: 2, c: 3
