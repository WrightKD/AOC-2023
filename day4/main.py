data = open('input.txt')

scratchcards = []

for line in data:
    win_count = 0

    row = line.rstrip()
    win_nums, nums = row.split(' | ')
    card, win_nums = win_nums.split(': ')
    win_nums = win_nums.split()
    nums = nums.split()

    scratchcards.append({"win_nums" : win_nums, "nums" : nums, "card" : card})


def get_win_count(scratchcard):
    win_count = 0

    win_nums = scratchcard["win_nums"]
    nums = scratchcard["nums"]

    for win in win_nums:
        if win in nums:
            win_count += 1

    return win_count


original_scratchcards = len(scratchcards)

for i in range(0, len(scratchcards)):
    scratchcards[i]["win_count"] = get_win_count(scratchcards[i])


def get_scratchcards(scratchcards):

    new_scratchcards = []

    for i in range(0,len(scratchcards)):
        win_count = scratchcards[i]['win_count']
        new_scratchcards += get_scratchcards(scratchcards[i+1:i+win_count+1])

    scratchcards += new_scratchcards
    return scratchcards
        

#print(len(get_scratchcards(scratchcards))+original_scratchcards)