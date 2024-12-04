'''
input= [['MMMSXXMASM'],
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

with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]


def count_word_in_grid(grid, word):
    rows, cols = len(grid), len(grid[0])
    
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]  
    
    def is_within_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def matches_from(x, y, dx, dy):
        for k in range(len(word)):
            nx, ny = x + k * dx, y + k * dy
            if not is_within_bounds(nx, ny) or grid[nx][ny] != word[k]:
                return False
        return True
    
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if matches_from(i, j, dx, dy):
                    count += 1
    
    return count



word = "XMAS"
print(count_word_in_grid(grid, word))  