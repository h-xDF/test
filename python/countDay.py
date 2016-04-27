from datetime import date,timedelta
enter = input().split()
BD = date(int(enter[0]),int(enter[1]),int(enter[2]))
today = date.today()
print(today - BD)
