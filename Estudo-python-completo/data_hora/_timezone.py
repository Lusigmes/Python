from datetime import datetime, timedelta, timezone

dataCC = datetime.now(timezone(timedelta(hours=2)))
dataSP = datetime.now(timezone(timedelta(hours=-3)))

print("Chicago:", dataCC)     
print("São Paulo:", dataSP)     