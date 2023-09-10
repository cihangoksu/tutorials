# %%
name_score_list = [['Harsh',20],['Beria',20],['Varun',19],['Kakunami',19],['Vikas',21]]

name_list, score_list = map(list, zip(*name_score_list))

score_list_sorted = score_list.copy()
score_list_sorted.sort()
second_max = score_list_sorted[0]
while second_max in score_list_sorted:
    score_list_sorted.remove(second_max)
second_max = score_list_sorted[0]

names_list = []
for idx, itemx in enumerate(score_list):
    if itemx == second_max:
        names_list.append(name_list[idx])

for nm in sorted(names_list):
    print(nm)


pass