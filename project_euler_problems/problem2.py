# O(n)

def even_valued():
    # Starting vals for the pointers
    curr_val = 2
    prev_val = 1
    seq = [1, 2]
    # while the current val is less than 4M (condition given in problem)
    while curr_val < 4000000:
        next_val = curr_val + prev_val
        seq.append(next_val)
        tmp = curr_val
        prev_val = tmp
        curr_val = next_val
    # the list seq holds the fibonacci sequence terms. To find the even ones just check if the remainder is 0 when
    # divided by 0
    print(seq)
    even_values = []
    for i in seq:                                   # O(len(seq)) => O(n)
        if i % 2 == 0:
            even_values.append(i)
    print(even_values)
    return sum(even_values)


print(even_valued())
