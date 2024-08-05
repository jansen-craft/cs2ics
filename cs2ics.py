import requests

TERM = "Fall%20Semester%202024-25"
COOKIE = ""

response = requests.get(
    f'https://ohio.collegescheduler.com/api/term-data/{TERM}',
    headers={'Cookie': COOKIE}
)

if("text/html" in response.headers['Content-Type']):
    raise Exception("Error: You need to update the COOKIE")

current_sections = response.json()["currentSections"]

for section in current_sections:
    title = section["title"]
    course = f'{section["subject"]}  {section["course"]}'
    instructor = section["instructor"][0]["name"] if section["instructor"] else "N/A"
    meetings = section["meetings"]
    days = meetings[0]["days"]
    startTime = meetings[0]["startTime"]
    endTime = meetings[0]["endTime"]
    startDate = meetings[0]["startDate"]
    endDate = meetings[0]["endDate"]
    room = meetings[0]["building"]
    
    print(title, course, instructor)
    print(f"\t{days}")
    print(f"\t{startTime} - {endTime}")
    print(f"\t{startDate} - {endDate}")
    print(f"\t{room}")
    