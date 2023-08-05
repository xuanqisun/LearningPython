def twoSum( nums_List, target ):
    n = len(nums_List)
    for index in range( n - 1): #range（）范围左闭右开不要忘

        for j in range(index + 1, n):
            result = int(nums_List[index]) + int(nums_List[j])

            if result == target:
                return [index,j]


print(twoSum([8,19,26,5,69,18],23))