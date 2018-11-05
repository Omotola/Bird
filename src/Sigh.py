"""
Print n rows of Pascal's Triangle.
The end points are always 1's.
Each interior number is the sum of
 the numbers above it.

For n=6
Print:
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
1 5 10 10 5 1
"""
def recursiveHelper(lis, n, target):

    if n <= target:
        result = []
        if n == 1:
            result.append(1)
            print(result)
        else:
            for i in range(n):
                if (i==0 or i==n-1):
                    result.append(1)
                else:
                    result.append(lis[i-1]+lis[i])
            print(result)
        recursiveHelper(result,n+1,target)


def pascal(n):
    # Recursive
    recursiveHelper([],1,n)

    # ITERATIVE
    # result = []
    # for i in range(0, n):
    #     new_result = []
    #     for j in range(0, i+1):
    #         if j == 0 or j == i:
    #             new_result.append(1)
    #         else:
    #
    #             sum = result[j] + result[j - 1]
    #             new_result.append(sum)
    #     print(new_result)
    #     result = new_result


print(pascal(6))