from _testcapi import INT_MIN


def kadane(a):
    max_so_far=INT_MIN
    max_ending_here=0

    for i in range(len(a)):
        max_ending_here=max_ending_here+a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here=0
    return max_so_far

a=list(map(int,input().split()))
print(kadane(a))
