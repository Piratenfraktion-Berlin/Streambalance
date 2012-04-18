# Create your views here.

from django.shortcuts import render_to_response
from django.db import connection, transaction

cursor = connection.cursor()
cursor.execute("SELECT SUM(slots) AS summe FROM django.icecast_balancer_mount WHERE name LIKE 'piratenfraktion.mp3' AND slots != 0 GROUP BY name;")
freeslots = cursor.fetchone()
cursor.execute("SELECT SUM(availableslots) AS summe FROM django.icecast_balancer_mount WHERE name LIKE 'piratenfraktion.mp3' AND slots != 0  GROUP BY name;")
slotsavailable = cursor.fetchone()

if freeslots == None:
	fsint = 0
	saint = 0
	listeners = 0
else:
        fsint = int(freeslots[0])
        saint = int(slotsavailable[0])
        listeners = saint-fsint
def frontpage(request):
    return render_to_response('frontpage.html',{'slotsavailable': saint, 'freeslots': fsint, 'listeners': listeners})
