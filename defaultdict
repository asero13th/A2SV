# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
val1, val2 = map(int,input().split())

A = [input() for i in range(val1)]
B = [input() for i in range(val2)]

val_a = defaultdict(lambda: ['-1'])

for idx,val in enumerate(A):
    if val in val_a:
        val_a[val].append(str(idx + 1))
    else:
        val_a[val] = [str(idx + 1)]
        
for val in B:
    print(' '.join(val_a[val]))

    
