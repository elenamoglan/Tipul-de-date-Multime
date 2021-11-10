"""from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1)) 
print('Toate submulţimile mulţimii {1, 2, 3, 4}:', set(powerset([1,2,3,4])))
print('Toate submulţimile mulţimii {’A’, ’B’, ’C’, ’D’}:', set(powerset(['A','B','C','D'])))"""

#Problema 10
S = {1, 2, 3, 4}
S=list(S)
len_S = len(S)
print('Toate submulţimile mulţimii {1, 2, 3, 4}: ', end='')
for i in range(1 << len_S):
    subset = {S[bit] for bit in range(len_S) if i & (1 << bit)}
    print(subset, end=',')

#Problema 11
S={'A', 'B', 'C', 'D'}
S=list(S)
len_S = len(S)
print('\nToate submulţimile mulţimii {’A’, ’B’, ’C’, ’D’}: ', end='')
for i in range(1 << len_S):
    subset = {S[bit] for bit in range(len_S) if i & (1 << bit)}
    print(subset, end=',')
