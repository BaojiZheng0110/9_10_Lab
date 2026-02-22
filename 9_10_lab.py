import ast

#s = input
#right_part = s.split("=", 1)[1].strip()
#lst = ast.literal_eval(right_part)



def is_worked(lst):
    lst.sort(key=lambda x: x[0])
    for i in range(len(lst) - 1):
        if lst[i][1] > lst[i+1][0]:
            return False
        else:
            return True

print(is_worked([[0,30],[5,10],[15,20]]))
print(is_worked([[7,10],[2,4]]))

#valid
print(is_worked([[1, 2], [3, 4], [5, 6]]))
print(is_worked([[0, 1], [2, 3]]))
print(is_worked([[5, 10], [11, 15], [20, 25]]))

#unvalid
print(is_worked([[1, 5], [4, 8]]))
print(is_worked([[0, 10], [2, 3]]))
print(is_worked([[3, 6], [1, 4]]))
print(is_worked([[1, 4], [2, 3], [5, 7]]))

#edge
print(is_worked([[1, 10], [10, 12]]))