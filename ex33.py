#while循环
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")
    print("The numbers: ")

    for num in numbers:
        print(num)

#for循环只能对一些东西进行循环，while循环可以对任何对象进行循环。