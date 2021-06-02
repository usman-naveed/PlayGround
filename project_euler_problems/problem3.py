# O(n^2 + n) => O(n^2)
# terrible lol :/

def largest_prime_factor(n):
    count_nums = dict()
    prime_nums_factors = []
    # These loops create the pairs of numbers that allow us to determine if i is prime. (only creates pairs < n/2,
    # since we know anything more than half the value cannot divide evenly into it) e.g pairs generated of 5 will be
    #  (5,2). If i is divisible by j, increase its count in the hashtable (count_nums). Therefore,
    # all the nums with count 0 in count_nums are prime nums.
    for i in range(1, n // 2):
        count_nums[i] = 0
        if i % 2 == 0 or i % 5 == 0:
            count_nums[i] += 1
            continue
        else:
            for j in range(i // 2, 1, -1):  # O(n^2)
                # print(i, j)
                if i % j == 0:
                    count_nums[i] += 1
                    break
                else:
                    pass

    for i in count_nums:  # O(n)
        if count_nums[i] == 0 and n % i == 0:
            prime_nums_factors.append(i)
    print(prime_nums_factors)
    return max(prime_nums_factors)


print(largest_prime_factor(600851475143))
