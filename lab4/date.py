#1 exercise

from datetime import datetime,timedelta 
current_time=datetime.today()
substructed_time=current_time-timedelta(5)
print("Today's date :", current_time.strftime("%Y-%m-%d"))
print("Date 5 days before:", substructed_time.strftime("%Y-%m-%d"))

#2 exerscise

from datetime import datetime,timedelta
current_time=datetime.today()
yesterday=current_time-timedelta(1)
tommorow=current_time+timedelta(1)
print("Yesterday's date was:",yesterday.strftime("%Y-%m-%d"))
print("Today's date is:",current_time.strftime("%Y-%m-%d"))
print("Tommorows's date will be:",tommorow.strftime("%Y-%m-%d"))

#3 exercise

from datetime import datetime
time=datetime.now()
without_millisec=time.strftime("%Y-%m-%d,%H:%M:%S")  #code automatically doesn't take milliseconds
print(without_millisec)


#4 exercise


from datetime import datetime,timedelta
yesterday = datetime.now() - timedelta(1)
tomorrow = datetime.now() + timedelta(1)
difference=tomorrow-yesterday   #разница между датами 2
print(difference.total_seconds()) #преобразуем разницу в секунды с помощью тотал секондс 

