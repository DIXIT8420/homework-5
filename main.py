from datetime import datetime

now = datetime.now()

print("Поточна дата:", now.strftime("%d.%m.%Y"))
print("Поточний час:", now.strftime("%H:%M:%S"))
