#ls1 = [3,4,2,1,3,3]
#ls2 = [4,3,5,3,9,3]

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
score = 0

while i < len(ls1):
    similarity = ls2.count(ls1[i])
    score += similarity * ls1[i]
    i += 1

print(score)

     

