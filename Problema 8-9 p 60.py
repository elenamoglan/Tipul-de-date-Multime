#Problema 8
A = set(map(int,input('Introduceti numerele multimii A: ').split(',')))
B = set(map(int,input('Introduceti numerele multimii B: ').split(',')))
print('a) intersecţia mulţimilor A şi B:', A.intersection(B))
print('b) reuniunea mulţimilor A şi B:', A.union(B))
print(f'c) diferenţa mulţimilor A şi B: {A.difference(B)} (A-B), {B.difference(A)} (B-A)\n')
#Problema 9
A = set(map(str,input('Introduceti literele mari ale multimii A: ').split(',')))
B = set(map(str,input('Introduceti literele mari ale multimii B: ').split(',')))
print('a) intersecţia mulţimilor A şi B:', A & B)
print('b) reuniunea mulţimilor A şi B:', A | B)
print(f'c) diferenţa mulţimilor A şi B: A/B - {A-B}, B/A - {B-A}')
