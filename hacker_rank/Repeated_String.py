# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    if len(s) < 2 and s == 'a':
        return n
    a_counter = 0
    a_remaining = 0
    for char in s:
        if char == 'a':
            a_counter += 1
    times_repeated_full = n // len(s)
    remaining_chars = n % len(s)
    for i in range(remaining_chars):
        if s[i] == 'a':
            a_remaining += 1
    a_counter = (times_repeated_full * a_counter) + a_remaining
    return a_counter
