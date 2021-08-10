sequence = [-13, -15, 13, 19, 18, 14, -5, 11, -13, 32, -33, -5, -1, -77, 78, -79]

sum_of_seq = count = max_seq = result = 0

for num in sequence:
    if num < 0:
        sum_of_seq += num
        count += 1
    else:
        if count > max_seq:
            max_seq = count
            result = sum_of_seq
        sum_of_seq = 0
        count = 0

print(result)