import calendar
month,day, year = map(int,input().split())
# year,month,day = 2010, 11,21

week_headers = calendar.weekheader(100)
week_names = list(week_headers.split())

asked_day_index =calendar.weekday(year,month,day)

print(week_names[asked_day_index].upper())

pass