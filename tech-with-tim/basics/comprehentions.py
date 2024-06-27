#A one line initlization of variavles in one line

x = [x + 5 for x in range(5)]
print(x)

nested_lists = [[i for i in range(4) ] for x in range(5) ]

conditional_list = [i for i in range(4) if i % 2 == 0 ]
conditional_set = {i for i in range(4) if i % 2 == 0}
generator_set = tuple(i for i in range(4) if i % 2 == 0)