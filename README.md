# CollegeScheduler to ICS

Export CollegeScheduler schedules to your calendar

Using the built in [api](https://ohio.collegescheduler.com/api), this script grabs your class information and produces a [.ics](https://en.wikipedia.org/wiki/ICalendar) file

# Setup

1. Go to [CollegeScheduler](https://ohio.collegescheduler.com)
   ![image](https://github.com/user-attachments/assets/750a90bb-8f6d-4622-a9af-336475317b9a)
3. Click on the term and campus you want to use
4. Inspect the page and load the Network tab
5. Click on this request
   ![image](https://github.com/user-attachments/assets/558113c8-9606-4539-8ac0-b8085c5b935c)
6. Copy your Cookie
   ![image](https://github.com/user-attachments/assets/ef26cf1d-2f3d-4c18-ab2a-05d6bc3de738)
8. Place into the COOKIE variable in cs2ics.py

# Running the script
```bash
    python cs2ics.py
```
You can now import the .ics file into most modern Calendar services (Outlook, Google Calendar etc...)
   
# Using the .ics file (Outlook Web)
1. Go to `Calendar` tab
2. Click `Add Calendar`
3. Click `Upload from file`
4. Select `classes.ics`
