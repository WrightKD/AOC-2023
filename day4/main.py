data = open('input.txt')

total_points = 0

for line in data:
    win_count = 0

    row = line.rstrip()

    win_nums, nums = row.split(' | ')

    card, win_nums = win_nums.split(': ')

    win_nums = win_nums.split()
    nums = nums.split()
    
    for i in win_nums:
        if i in nums:
            win_count += 1

    if win_count > 0:
        total_points += 2**(win_count-1)

print("Total Points : ", total_points)