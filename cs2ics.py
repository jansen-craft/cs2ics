from icalendar import Calendar, Event
import requests
from datetime import datetime, timedelta

DAY_MAP = {"M": "MO", "T": "TU", "W": "WE", "R": "TH", "F": "FR"}
TERM = "Fall%20Semester%202024-25"
COOKIE = ""

response = requests.get(
    f'https://ohio.collegescheduler.com/api/term-data/{TERM}',
    headers={'Cookie': COOKIE}
)

if("text/html" in response.headers['Content-Type']):
    raise Exception("Error: You need to update the COOKIE")

current_sections = response.json()["currentSections"]

calendar = Calendar()

for section in current_sections:
    title = section["title"]
    course = f'{section["subject"]}  {section["course"]}'
    instructor = section["instructor"][0]["name"] if section["instructor"] else "N/A"
    meeting = section["meetings"][0]
    days = meeting["daysRaw"]
    startTime = datetime.strptime(str(meeting["startTime"]), "%H%M").time()
    endTime = datetime.strptime(str(meeting["endTime"]), "%H%M").time()
    startDate = datetime.strptime(str(meeting["startDate"]), "%Y-%m-%dT%H:%M:%S%z")
    endDate = datetime.strptime(str(meeting["endDate"]), "%Y-%m-%dT%H:%M:%S%z")
    room = meeting["building"]

    start = datetime.combine(startDate, startTime)
    end = datetime.combine(startDate, endTime)
    bydays = [DAY_MAP[day] for day in DAY_MAP if day in days]

    event = Event()
    event.add('summary', f"{course} {title}")
    event.add('dtstart', start)
    event.add('dtend', end)
    event.add('location', room)
    event.add('description', f"Instructor: {instructor}")
    event.add('RRULE', {'FREQ':["WEEKLY"], 'UNTIL':endDate + timedelta(days=1), 'BYDAY':bydays})
    calendar.add_component(event)

with open('classes.ics', 'wb') as f:
    f.write(calendar.to_ical())