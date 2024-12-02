
'''
ls = [[7,6,4,2,1],
       [1,2,7,8,9],
       [9,7,6,2,1],
       [1,3,2,4,5],
       [8,6,4,4,1],
       [1,3,6,7,9]]


'''
ls = []

with open('input.txt', 'r') as file:
    for line in file:
        numbers = line.strip().split()  
        row = [int(num) for num in numbers]  
        ls.append(row)



safe = 0

check = 0

safe_before = []

for v in ls:
    if all(k < l for k, l in zip(v, v[1:])) is True or all(k > l for k, l in zip(v, v[1:])) is True:
        count = 0
        i = 0        
        while i < len(v):
            if i < len(v)-1 and (v[i+1] - v[i] > 0 and v[i+1] - v[i] < 4):
                count += 1
            if i < len(v)-1 and (v[i] - v[i+1] > 0 and v[i] - v[i+1] < 4):
                count += 1
            i += 1
        if count == len(v)-1: 
            safe_before.append(v)



checking = []

for y in ls:
    if y not in safe_before:
        checking.append(y)



subsets = []

for value in checking:
    og_ls = []
    for e in range(len(value)):
        part_before = value[:e]
        part_after = value[e+1:]
        subset = part_before + part_after
        og_ls.append(subset)
    subsets.append(og_ls)



check = []
for h in subsets:
    if h in check:
        exit
    else:
        for v in h:
            if all(k < l for k, l in zip(v, v[1:])) is True or all(k > l for k, l in zip(v, v[1:])) is True:
                count = 0
                i = 0        
                while i < len(v):
                    if i < len(v)-1 and (v[i+1] - v[i] > 0 and v[i+1] - v[i] < 4):
                        count += 1
                    if i < len(v)-1 and (v[i] - v[i+1] > 0 and v[i] - v[i+1] < 4):
                        count += 1
                    i += 1
                if count == len(v)-1: 
                    check.append(h)
    
            
            

unique_list = []
for item in check:
    if item not in unique_list:
        unique_list.append(item)

safe = len(unique_list)
        
new_safe = safe + len(safe_before)

print(new_safe)




