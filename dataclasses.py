from datetime import datetime, timedelta

date_string = "21 June, 2018"

print("date_string =", date_string)
print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)
print("type of date_object =", type(date_object))

now = datetime.now()


# 1.Write a program that reads in a number and prints the date that number of days from now in this format: Saturday,
# February 06, 2021.

first_date = datetime.now()
days = int(input())
end_date = first_date + timedelta(days=days)
print(datetime.strftime(end_date, "%A, %B, %d, %Y"))
