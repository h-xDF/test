from datetime import date, timedelta
enter = input().strip().split()
today = date(int(enter[0]),int(enter[1]),int(enter[2]))
today = today + timedelta(days = int(input()))
print(str(today.year) +" "+ str(today.month) +" "+ str(today.day))
