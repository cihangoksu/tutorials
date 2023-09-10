'''
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
'''

from statistics import mean

def get_average(query_name, student_marks):
    avg = 0
    for key, value in student_marks.items():
        if key == query_name:
            avg = mean(value)
    return avg



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    avg_value = get_average(query_name, student_marks)
    print("%.2f" % avg_value)




