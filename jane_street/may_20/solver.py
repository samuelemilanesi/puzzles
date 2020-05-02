max_col = 10000
def extend(row):
    return list(row)+[k for k in range(row[-1]+1,max_col)]

def build_next_row(prev_row, index_row):

    prev = extend(prev_row)
    new_row = []
    
    count = 1
    for i in range(index_row):
        new_row.append(prev[index_row-count])
        new_row.append(prev[index_row+count])
        count += 1

    return extend(new_row)

row = list(range(2,25))
index = 1
while row[index] != 11:
    row = build_next_row(row, index)
    index += 1
print(index+1)