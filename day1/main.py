from collections import OrderedDict
import re

chall_input = open('input.txt')

sums = 0

digit_map = OrderedDict()
digit_map["nine"]  = "9"
digit_map["eight"] = "8"
digit_map["seven"] = "7"
digit_map["six"]   = "6"
digit_map["five"]  = "5"
digit_map["four"]  = "4"
digit_map["three"] = "3"
digit_map["two"]   = "2"
digit_map["one"]   = "1"

digit_map_reverse = dict((v,k) for k,v in digit_map.items())

# Loop through each line and remove extra line character with rstrip() 55194
for line in chall_input:
    line = line.rstrip()
    original_line = line

    low_index = 1000
    high_index = -1

    first_value = None
    last_value = None

    for k in digit_map:
        if k in line:
            current_index = line.index(k)
            if current_index > high_index:
                high_index = current_index
                last_value = k
            if current_index < low_index:
                low_index = current_index
                first_value = k

    if first_value:
        line = line.replace(first_value, digit_map[first_value])

    if last_value:
        line = line.replace(last_value, digit_map[last_value])

    result = re.sub(r'[^0-9]', '', line)
    result = f"{result[0]}{result[-1]}"

    if not first_value or not last_value:
        print("First in Line : ", first_value)
        print("Last in Line : ", last_value)
        print(line, original_line, "Result : " , result)

    sums += int(result)

print(sums)