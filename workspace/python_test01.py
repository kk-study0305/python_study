import datetime

# 日付をyyyy/mm/dd形式で指定
today_date = "2023/01/28"
days_monthly = [31,28,31,30,31,30,31,31,30,31.30,31]
days_monthly_leap = [31,29,31,30,31,30,31,31,30,31.30,31]

date_split = today_date.split('/')
today_year = int(date_split[0])
today_month = int(date_split[1])
today_day = int(date_split[2])
print(f'今日は{today_year}年{today_month}月{today_day}日です。')

# 閏年のチェック
if (today_year % 4 == 0 and today_year % 100 != 0) or (today_year % 400 == 0):
    uruu_check = True
else :
    uruu_check = False

total_days = 0
tmp_days = 0
last_days = 0
if uruu_check:
    print('今年は閏年です。')
    for i in range(today_month - 1):
        if today_month != 1:
            tmp_days = tmp_days + days_monthly_leap[i]
    total_days = tmp_days + today_day
    last_days = 366 - today_day + 1
else :
    print('今年は平年です。')
    for i in range(today_month - 1):
        if today_month != 1:
            tmp_days = tmp_days + days_monthly[i]
    total_days = tmp_days + today_day
    last_days = 365 - today_day + 1
print(f'今日は{total_days}日目です。')
print(f'今年は残り{last_days}日です。')
