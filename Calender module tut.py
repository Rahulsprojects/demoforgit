import calendar
m, d, y = map(int, input().split())
weekday_num = calendar.weekday(y, m, d)
week_list = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
for i in range(len(week_list)):
    if i == weekday_num:
        print(week_list[i])
        break


