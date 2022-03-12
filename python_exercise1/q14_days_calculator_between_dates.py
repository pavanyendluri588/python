from datetime import date
#takeing date as string
first_date=str(input("Enter the first date:"))
last_date=str(input("Enter the last date:"))
#spliting string according to commas
x_split=first_date.split(",")
print(x_split)
#converting the string list to int list
x_li = []
for i in x_split:
	x_li.append(int(i))

y_split=last_date.split(",")
print(y_split)
y_li = []
for i in y_split:
	y_li.append(int(i))
f_date=date(x_li[0],x_li[1],x_li[2])
l_date=date(y_li[0],y_li[1],y_li[2])
cal=f_date-l_date
print("remainf days is:",cal.days)