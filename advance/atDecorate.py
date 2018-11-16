import datetime

"""
decorator function
with parameter if function to be decorated has parameter
"""
def print_today(gift):
    print(datetime.datetime.now()) 
    return gift


@print_today
def my_decorator(gift:str = "Teddy Bear"):
    today = datetime.datetime.now()
    xmas = datetime.datetime(today.year,12,25)
    if today > xmas:
        print("Almost new year")
    else:
        if (xmas-today).days < 50:
            print("buy a xmas gift. " + gift)
        else:
            print("long way to the end")

# will print datetime now first
my_decorator("Spider Man")
my_decorator("PS4")
my_decorator()