count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

result = 0
mapped_list = []

verite = [[0 for i in range(9)] for j in range(512)]
for i in range(512):
    count1 += 1
    count2 += 1
    count3 += 1
    count4 += 1
    count5 += 1
    count6 += 1
    count7 += 1
    count8 += 1
    count9 += 1
    for j in range(9):
        if count1 > 512:
            count1 = 1
        elif count2 > 256:
            count2 = 1
        elif count3 > 128:
            count3 = 1
        elif count4 > 64:
            count4 = 1
        elif count5 > 32:
            count5 = 1
        elif count6 > 16:
            count6 = 1
        elif count7 > 8:
            count7 = 1
        elif count8 > 4:
            count8 = 1
        elif count9 > 2:
            count9 = 1
        
        if count1 <= 256 and j == 0:
            verite[i][j] = 1
        elif count2 <= 128 and j == 1:
            verite[i][j] = 1
        elif count3 <= 64 and j == 2:
            verite[i][j] = 1
        elif count4 <= 32 and j == 3:
            verite[i][j] = 1
        elif count5 <= 16 and j == 4:
            verite[i][j] = 1
        elif count6 <= 8 and j == 5:
            verite[i][j] = 1
        elif count7 <= 4 and j == 6:
            verite[i][j] = 1
        elif count8 <= 2 and j == 7:
            verite[i][j] = 1
        elif count9 <= 1 and j == 8:
            verite[i][j] = 1
        else:
            verite[i][j] = 0

            
for i in range(len(verite)):
    if sum(verite[i]) == 5:
        mapped_list.append(sum(verite[i]))
print(mapped_list)
print(len(mapped_list))