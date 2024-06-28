from datetime import date, datetime
import pytz

day = datetime .now()
data = datetime.now(pytz.timezone("America/Sao_Paulo")) #Fuzohorario
data2 = datetime.now(pytz.timezone("Europe/Oslo"))
# data = date (2024, 7, 10)
# print(data)
print (date.today())
print(datetime.today())
print(day.strftime("%d/%m/%Y %H:%M")) #9/6/2024 10:42
print("----------------------")
print(data)
print(data2)
print("----------------------")

