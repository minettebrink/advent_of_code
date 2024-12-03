



ls1 = []
ls2 = []

# Open and read the file
with open('input.txt', 'r') as file:
    for line in file:
        # Split the line into two numbers
        numbers = line.strip().split()
        if len(numbers) == 2:  
            ls1.append(int(numbers[0])) 
            ls2.append(int(numbers[1]))


ls1.sort()
ls2.sort()

i = 0
distance = 0

while i < len(ls1):
    if ls1[i] > ls2[i]:
        distance += ls1[i] - ls2[i]
    else: 
        distance += ls2[i] - ls1[i]
    i += 1

print(distance)
     

