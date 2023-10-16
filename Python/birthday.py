from datetime import date
from data import data

todays_date = date.today()
todays_day = todays_date.day
todays_month = todays_date.month

for user in data:
    user_date = user['birthday'].split('-')
    user_birth_date = date(int(user_date[0]),int(user_date[1]),int(user_date[2]))
    user_birth_day = user_birth_date.day
    user_birth_month = user_birth_date.month
    
    if user_birth_day == todays_day and user_birth_month == todays_month:
        print(f"Wish {user['name']} a happy birthday!")