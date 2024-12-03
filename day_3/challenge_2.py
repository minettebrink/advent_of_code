import re
#text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("input.txt", "r") as file:  
    text = file.read()  


 
pattern = r"mul\(-?\d+,-?\d+\)|do\(\)|don't\(\)"

dos_donts = re.findall(pattern, text)

mul = []
collect = True

for item in dos_donts:
    if item == "don't()":
        collect = False  
    elif item == "do()":
        collect = True  
        continue
    if collect:
        mul.append(item)



sum = 0
for i in mul: 
    numbers = re.findall(r'\d+', i)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    sum += numbers[0] * numbers[-1]

print(sum)








        
    


        



    
    

    