import requests

TERM = "Fall%20Semester%202024-25"
COOKIE = ""

response = requests.get(
    f'https://ohio.collegescheduler.com/api/term-data/{TERM}',
    headers={'Cookie': COOKIE}
)