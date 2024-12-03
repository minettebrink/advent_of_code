import re
#text = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

with open("input.txt", "r") as file:  
    text = file.read()  


 
pattern = r"mul\(-?\d+,-?\d+\)"

mul = re.findall(pattern, text)


sum = 0
for i in mul: 
    numbers = re.findall(r'\d+', i)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    sum += numbers[0] * numbers[-1]

print(sum)








        
    


        



    
    

    