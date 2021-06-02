#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    if n < 2:
        return 0
    hash_table = {}
    for i in ar:
        if i in hash_table:
            hash_table[i] += 1
        else:
            hash_table[i] = 1
    return sum([x//2 for x in hash_table.values()])
