data = open('input.txt')
grid = []

for line in data:
    row = [x for x in line.rstrip()]
    grid.append(row)

size = 140
numbers_with_symbol = []
part_numbers = []

part_number_details = []

gear_ratio = {}

for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
        
        # check adjecnt 
        up = i - 1
        right = j + 1
        left = j - 1
        down = i + 1

        character = grid[i][j]

        down_range = False
        top_range = False

        if character != '.' and not character.isnumeric():

            tl = grid[up][left] if up >= 0 and left >= 0 else '.'
            t = grid[up][j] if up >= 0 else '.'
            tr = grid[up][right] if up >= 0 and right < size else '.'

            l = grid[i][left] if left >= 0 else '.'
            r = grid[i][right] if right < size else '.'

            dl = grid[down][left] if down < size and left >= 0 else '.'
            d = grid[down][j] if down < size else '.'
            dr = grid[down][right] if down < size and right < size else '.'

            # print("--------------------------------------------------")

            # print(tl, t, tr)
            # print(l, character, r)
            # print(dl, d, dr)

            # character_grid = [
            #     [tl, t, tr],
            #     [l, character, r],
            #     [dl, d, dr]
            # ]

            if t.isnumeric():
                numbers_with_symbol.append((up,j,character, i, j))
            else:
                if tl.isnumeric():
                    numbers_with_symbol.append((up,left,character, i, j))
                if tr.isnumeric():
                    numbers_with_symbol.append((up,right,character, i, j))

            if l.isnumeric():
                numbers_with_symbol.append((i,left,character, i, j))

            if r.isnumeric():
                numbers_with_symbol.append((i,right,character, i, j))

            if d.isnumeric():
                numbers_with_symbol.append((down,j,character, i, j))
            else:
                if dl.isnumeric():
                    numbers_with_symbol.append((down,left, character, i, j))
                if dr.isnumeric():
                    numbers_with_symbol.append((down,right, character, i, j))
                
for n in numbers_with_symbol:
    x,y,c,i,j = n
    number = grid[x][y]
    start = number

    while y > 0:
        y -= 1
        if not grid[x][y].isnumeric():
            break
        number = grid[x][y] + number

    x,y,c,i,j = n
    while y < size - 1:
        y += 1
        if not grid[x][y].isnumeric():
            break
        number = number + grid[x][y]

    x,y,c,i,j = n
    part_number_details.append((x,y,c,number,i,j))

        
for i in range(0, len(part_number_details)):
    part_one = part_number_details[i]
    x_1,y_1,c_1,n_1, k, l = part_one

    if c_1 != '*':
        continue

    character_loc = f"{k},{l}"
    
    if character_loc in gear_ratio:
        gear_ratio[character_loc].append(int(n_1))
    else:
        gear_ratio[character_loc] = [int(n_1)]

gear_ratio_sum = 0

for gr in gear_ratio:
    if len(gear_ratio[gr]) == 2:
        ratios = gear_ratio[gr]
        print(gr, gear_ratio[gr])
        gear_ratio_sum += ratios[0] * ratios[1]


print("Gear Ratio Sum : ", gear_ratio_sum)