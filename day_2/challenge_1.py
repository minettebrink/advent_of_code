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
            safe += 1
    


print(safe)






