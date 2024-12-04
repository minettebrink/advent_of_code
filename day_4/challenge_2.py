
'''
ls= [['MMMSXXMASM'],
        ['MSAMXMSMSA'],
        ['AMXSXMAAMM'],
        ['MSAMASMSMX'],
        ['XMASAMXAMM'],
        ['XXAMMXXAMA'],
        ['SMSMSASXSS'],
        ['SAXAMASAAA'],
        ['MAMMMXMMMM'],
        ['MXMXAXMASX']]
'''
#grid = [list(sublist[0]) for sublist in ls]

with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]



def find_mas_x_shape(grid):
    rows, cols = len(grid), len(grid[0])  
    count = 0  
    
    for i in range(1, rows - 1):  
        for j in range(1, cols - 1):  
            if grid[i][j] == 'A':  
                
                if (
                    (grid[i - 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S' and  
                    grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S') or     
                    (grid[i - 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M' and  
                    grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M') or
                    (grid[i - 1][j - 1] == 'S' and grid[i + 1][j + 1] == 'M' and  
                    grid[i - 1][j + 1] == 'M' and grid[i + 1][j - 1] == 'S')  or
                    (grid[i - 1][j - 1] == 'M' and grid[i + 1][j + 1] == 'S' and  
                    grid[i - 1][j + 1] == 'S' and grid[i + 1][j - 1] == 'M')  
                ):
                    count += 1
    
    return count


print(find_mas_x_shape(grid))  