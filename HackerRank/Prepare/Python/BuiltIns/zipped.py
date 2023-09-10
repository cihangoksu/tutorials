# %%
# myzip = zip([1,2,3,4,5,6],'Hacker')
# print(list(myzip))

# %%

student1 = [89,90,78,93,80]
student2 = [90,91,85,88,86]
student3 = [91,92,83,89,90.5]

zipped_students = zip(student1,student2, student3)
for grades in zipped_students:
    avg_grade = sum(grades)/len(grades)
    print(avg_grade)

