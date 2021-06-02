#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    start_points = []
    sum_all_hourglass = []
    hourglass = []
    for i in range(4):
        for j in range(4):
            tmp = [i, j]
            start_points.append(tmp)

    for i in start_points:
        hourglass.append(arr[i[0]][i[1]])
        hourglass.append(arr[i[0]][i[1] + 1])
        hourglass.append(arr[i[0]][i[1] + 2])
        hourglass.append(arr[i[0] + 1][i[1] + 1])
        hourglass.append(arr[i[0] + 2][i[1]])
        hourglass.append(arr[i[0] + 2][i[1] + 1])
        hourglass.append(arr[i[0] + 2][i[1] + 2])
        sum_all_hourglass.append(sum(hourglass))
        hourglass = []
    print(hourglass)

    return max(sum_all_hourglass)
