import requests, re, datetime
from bs4 import BeautifulSoup
# from .serializers import EventsSerializer

import django
month = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}

response = requests.get("https://timesofindia.indiatimes.com/sports/cricket/ipl/schedule")
soup = BeautifulSoup(response.text, "lxml")
matches = soup.find_all('div', attrs={"class": "matchdetails"})

def get_data():
    django.setup()
    from .models import Events
    def setDateTime(date, t):
        _ = re.search(r'(.{2}):(.{2})', t)
        
        date_string = date[3] + '-' + month[date[2]] + '-' + date[1] + ' '+ _.group(1) + ':' + _.group(2)
        date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M')
        return date_obj
        
        # print(tt.group(1) + tt.group(2))

    for match in matches:
        info = match.find_all('div',"match-teams")
        start_time = match.find('div',attrs={"class": "match-meta"}).get_text()
        date = info[0].get_text().split(" ")
        date_time = setDateTime(date, start_time)
        teams = info[1].get_text()

        Events(title=teams, start_date=date_time).save()
        print("t?")
    # date_time, teams
