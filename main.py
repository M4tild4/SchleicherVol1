from datetime import date
import datetime

start_datum = datetime.date(2023, 7, 16)
while date.today() == start_datum:
    print("Ich bin am ", date.today(), " der listige, verschlagener Schleicher: Fang mich, wenn Du kannst!")

