def flatten_list(lst):
    input = lst
    output = [] #[1, 2, 3, 4, 5, 6, 7]
    for i in input:

        output.append(input[i]) 
        print(output)

lst = [1, [2], [3, [4, 5, [6]]], 7]
print(flatten_list(lst))