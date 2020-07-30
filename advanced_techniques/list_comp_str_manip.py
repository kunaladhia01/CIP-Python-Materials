# Advanced techniques

# string manipulation
s = "Hello world"
print(len(s))

a = "Hello "
b = "world"
print(a+b)

# substrings
s = "Hello world"
print(s[:-2])

print(s[4:9])

# indexing
print(s[1])

t = "hello goodbye"
# print(t.index("good"))

x = "ifjdsoijhfioshfiodshoshfioashfiadshioshfajsf"
print(x.count('i'))
print(x.index('i'))

# list comprehension

s = 0
for i in range(101):
    s += i
print(s)

print(sum([i for i in range(101)]))

# [element for index in range(2)]

li = []
for i in range(1, 11):
    li.append(i ** 2)
print(li)

new_list = [i ** 2 for i in range(1, 11)]
print(new_list)

l1 = [i ** 2 for i in range(1, 20, 2)]
print(l1)
l2 = [i ** 2 for i in range(1, 20) if i % 2 == 1]
print(l2)


print(sum([i for i in range(1, 101) if i % 4 == 0]))
print(sum([i for i in range(0, 101, 4)]))
