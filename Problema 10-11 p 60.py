from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1)) 
print('Toate submulţimile mulţimii {1, 2, 3, 4}:', set(powerset([1,2,3,4])))
print('Toate submulţimile mulţimii {’A’, ’B’, ’C’, ’D’}:', set(powerset(['A','B','C','D'])))