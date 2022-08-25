from datetime import datetime, timedelta

tanggal = datetime.now()
tanggal2 = tanggal - timedelta(weeks=2)
print(tanggal2)