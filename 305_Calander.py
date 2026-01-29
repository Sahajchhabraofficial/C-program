#wap to convert specified days into years weeks and days.
day=int(input("enter number of days: "))#3835
years=day//365
day=day%365
months=day//30
day=day%30
week=day//7
day=day%7
print(f"Years: {years} Months: {months} week: {week} Day: {day}")
