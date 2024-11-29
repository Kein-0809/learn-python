# type()
hello_type = type("Hello")
print(hello_type)

# id()
hello = "hello"
hello2 = "hello"
world = "world"
print(id(hello))  # id1 (例)
print(id(hello2))  # id1 (例)
print(id("hello"))  # id1 (例)
print(id(world))  # id3 (例)