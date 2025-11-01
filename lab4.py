fight_complect = {
    'antidot': ['d', 1, 10],
}
fight_list = [
    ['r', 3, 25],
    ['p', 2, 15],
    ['a', 2, 15],
    ['m', 2, 20],
    ['i', 1, 5],
    ['k', 1, 15],
    ['x', 3, 20],
    ['t', 1, 25],
    ['f', 1, 15],
    ['s', 2, 20],
    ['c', 2, 20]]
surv_points = 15
cnt_surv = 0
count_cell = 9 - fight_complect['antidot'][1]
result = []
fight_list.sort(key=lambda x: (x[2]//x[1], x[1]), reverse=True)
for surv in fight_list:
    cnt_surv += surv[2]
for weapon in fight_list:
    if count_cell >= weapon[1]:
        count_cell -= weapon[1]
        surv_points += weapon[2]
        result.extend([weapon[0]] * weapon[1])
result.append(fight_complect['antidot'][0])
surv_points = surv_points - (cnt_surv - surv_points)

#matric
matric = []
for i in range(0, len(result), 3):
    row = result[i:i + 3]
    matric.append(row)

for row in matric:
    for element in row:
        print(f"[{element}]", end=" ")
    print()
print(f'Итоговые очки выживания: {surv_points}')
